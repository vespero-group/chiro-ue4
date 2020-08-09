"""Context utilities

Utility functions for working with Blender Addon API context
"""


import bpy
import os
import threading
from contextlib import contextmanager
from .fs import temp_file_ctx


_THREAD_LOCAL = threading.local()
_THREAD_LOCAL.context = None


@contextmanager
def with_blender_context(context=None):
    initial_context = _THREAD_LOCAL.context

    _THREAD_LOCAL.context = context

    try:
        yield

    finally:
        _THREAD_LOCAL.context = initial_context


@contextmanager
def selected_objects_ctx(objects=None):
    view_layer = get().view_layer
    initial_selected = [o for o in view_layer.objects if o.select_get and o.select_get(view_layer=view_layer)]

    for obj in view_layer.objects:
        if obj.select_set:
            obj.select_set(False, view_layer=view_layer)

    try:
        for obj in objects:
            obj.select_set(True, view_layer=view_layer)

        yield

    finally:
        for obj in view_layer.objects:
            if obj.select_set:
                obj.select_set(False, view_layer=view_layer)

        for obj in initial_selected:
            obj.select_set(True, view_layer=view_layer)


@contextmanager
def active_object_ctx(object_name=None):
    initial_object = get().view_layer.objects.active

    try:
        get().view_layer.objects.active = (
            bpy.data.objects[object_name] if object_name else None
        )
        yield

    finally:
        get().view_layer.objects.active = initial_object


def get_active_object():
    return get().view_layer.objects.active


def get():
    if _THREAD_LOCAL.context:
        return _THREAD_LOCAL.context
    else:
        return bpy.context


def get_object():
    return get().object


def get_pose():
    return get_object().pose


def get_scene_unit_scale():
    return get().scene.unit_settings.scale_length


def set_scene_unit_scale(scale):
    get().scene.unit_settings.scale_length = scale


@contextmanager
def scene_unit_scale(scale=None):
    initial_scale = get_scene_unit_scale()

    try:
        if scale is not None:
            set_scene_unit_scale(scale)
        yield

    finally:
        set_scene_unit_scale(initial_scale)


@contextmanager
def snapshot_then_rollback_ctx():
    with temp_file_ctx() as filepath:
        try:
            bpy.ops.wm.save_as_mainfile(copy=True, filepath=filepath)

            yield

        finally:
            if os.path.exists(filepath):
                bpy.ops.wm.recover_auto_save(filepath=filepath)
