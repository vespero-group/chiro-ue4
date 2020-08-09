"""Object utilities

Utility functions for working with Blender Addon API context
"""

import bpy
from contextlib import contextmanager
from mathutils import Vector
from . import context as ctx


def get_object_and_children():
    obj = ctx.get_object()
    return [obj] + [c for c in (obj.children if obj.children else ())]


@contextmanager
def scale_ctx(scale, unit_scale=None):
    the_object = ctx.get_object()
    initial_object_scale = the_object.scale.copy()

    if unit_scale is None:
        unit_scale = ctx.get_scene_unit_scale()

    with ctx.scene_unit_scale(unit_scale):
        try:
            the_object.scale = initial_object_scale * scale
            yield

        finally:
            the_object.scale = initial_object_scale


@contextmanager
def scale_applied_ctx_old(scale, unit_scale=None):
    the_object = ctx.get_object()
    initial_object_scale = the_object.scale.copy()
    initial_object_dimensions = the_object.dimensions.copy()

    with scale_ctx(scale, unit_scale):
        try:
            with ctx.selected_objects_ctx(get_object_and_children()):
                bpy.ops.object.transform_apply(
                    location=False, rotation=False, scale=True, properties=False)
            yield
        finally:
            the_object.scale = initial_object_scale
            the_object.dimensions = initial_object_dimensions


@contextmanager
def rotation_applied_ctx():
    the_object = ctx.get_object()
    initial_mode = the_object.rotation_mode
    # initial_axis = the_object.rotation_axis_angle
    initial_euler = the_object.rotation_euler.copy()
    initial_quat = the_object.rotation_quaternion.copy()

    try:
        the_object.rotation_mode = 'QUATERNION'
        applied_quat = the_object.rotation_quaternion.copy()
        applied_success = False
        with ctx.selected_objects_ctx(get_object_and_children()):
            bpy.ops.object.transform_apply(
                location=False, rotation=True, scale=False, properties=False)
        applied_success = True

        yield

    finally:
        if applied_success:
            the_object.rotation_quaternion = applied_quat.inverted()
            with ctx.selected_objects_ctx(get_object_and_children()):
                bpy.ops.object.transform_apply(
                    location=False, rotation=True, scale=False, properties=False)
            the_object.rotation_quaternion = applied_quat

        the_object.rotation_mode = initial_mode
        # the_object.rotation_axis_angle = initial_axis
        the_object.rotation_euler = initial_euler
        the_object.rotation_quaternion = initial_quat


@contextmanager
def applied_transforms_ctx():
    with location_applied_ctx():
        with rotation_applied_ctx():
            with scale_applied_ctx(1):
                yield


@contextmanager
def location_applied_ctx():
    the_object = ctx.get_object()
    initial_location = the_object.location.copy()

    try:
        applied_success = False
        with ctx.selected_objects_ctx(get_object_and_children()):
            bpy.ops.object.transform_apply(
                location=True, rotation=False, scale=False, properties=False)
        applied_success = True

        yield

    finally:
        if applied_success:
            the_object.location -= initial_location
            with ctx.selected_objects_ctx(get_object_and_children()):
                bpy.ops.object.transform_apply(
                    location=True, rotation=False, scale=False, properties=False)
        the_object.location = initial_location


@contextmanager
def scale_applied_ctx(unit_scale=None):
    the_object = ctx.get_object()

    initial_object_scale = the_object.scale.copy()

    try:
        with ctx.scene_unit_scale(unit_scale):
            if unit_scale:
                the_object.scale /= unit_scale

            with ctx.selected_objects_ctx(get_object_and_children()):
                bpy.ops.object.transform_apply(
                    location=False, rotation=False, scale=True, properties=False)

            yield

    finally:
        if not unit_scale:
            unit_scale = 1

        the_object.scale = Vector((
            (the_object.scale.x / initial_object_scale.x * unit_scale),
            (the_object.scale.y / initial_object_scale.y * unit_scale),
            (the_object.scale.z / initial_object_scale.z * unit_scale),
        ))
        with ctx.selected_objects_ctx(get_object_and_children()):
            bpy.ops.object.transform_apply(
                location=False, rotation=False, scale=True, properties=False)
        the_object.scale = initial_object_scale
