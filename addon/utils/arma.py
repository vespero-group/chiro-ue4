"""Armature utilities

Utility functions for operating on armatures
"""


import bpy
import itertools

from contextlib import contextmanager
from .context import get as get_context, get_object
from .mode import active_mode_ctx, MODE_EDIT
from .bone import EditBone
# from .transform import EditBone


PARENT_TYPE_CONNECTED = "CONNECTED"
PARENT_TYPE_OFFSET = "OFFSET"


def has_bone(bone_name):
    return bone_name in get_object().data.edit_bones


def get_bone(bone_name):
    return get_object().data.edit_bones[bone_name]


def create_bone(bone_name, parent_name=None, parenting_type=PARENT_TYPE_OFFSET):
    bpy.ops.armature.bone_primitive_add(name=bone_name)

    if parent_name:
        parent_bone(bone_name, parent_name, parenting_type)

    return get_bone(bone_name)


def parent_bone(bone_name, parent_name, parenting_type):
    with selected_bones_ctx([bone_name]):
        with active_bone_ctx(parent_name):
            bpy.ops.armature.parent_set(type=parenting_type)


def delete_bone(bone_name, delete_children=False):
    delete_names = []
    if delete_children:
        def get_children(bone):
            return \
                [bone.name] + \
                [b.name for b in bone.children] + \
                list(itertools.chain.from_iterable(
                    map(get_children, bone.children)))
        delete_names = get_children(get_bone(bone_name))
    else:
        delete_names = [bone_name]

    with selected_bones_ctx(delete_names):
        bpy.ops.armature.delete()


def unselect_bones():
    for bone in get_context().selected_editable_bones:
        bone.select = False


def snap_bone_to_bone(subject_bone_name, target_bone_name):
    subject = get_bone(subject_bone_name)
    target = get_bone(target_bone_name)

    offset = subject.head - target.head

    subject.head -= offset
    subject.tail -= offset


def disconnect_children(bone_name):
    with selected_bones_ctx([b.name for b in get_bone(bone_name).children]):
        bpy.ops.armature.parent_clear(type='DISCONNECT')


@contextmanager
def unselect_bones_ctx():
    initially_selected_bones = [
        bone for bone in get_context().selected_editable_bones if bone.select
    ]

    unselect_bones()
    try:
        yield
    finally:
        unselect_bones()
        for bone in initially_selected_bones:
            bone.select = True


def select_bones(selected_bone_names=None):
    for bone_name in (selected_bone_names if selected_bone_names else []):
        if has_bone(bone_name):
            get_bone(bone_name).select = True


@contextmanager
def selected_bones_ctx(selected_bone_names=None):
    with unselect_bones_ctx():
        for bone_name in (selected_bone_names if selected_bone_names else []):
            get_bone(bone_name).select = True
        yield


@contextmanager
def active_bone_ctx(bone_name):
    initial_active_bone = get_object().data.edit_bones.active

    bone = get_bone(bone_name)
    get_object().data.edit_bones.active = bone

    try:
        yield

    finally:
        get_object().data.edit_bones.active = initial_active_bone


def get_mirror_x():
    return get_object().data.use_mirror_x


def set_mirror_x(enabled):
    get_object().data.use_mirror_x = enabled


@contextmanager
def mirror_x_ctx(enabled=True):
    initial_enabled = get_mirror_x()

    set_mirror_x(enabled)

    try:
        yield

    finally:
        set_mirror_x(initial_enabled)


def get_armature_snapshot():
    with active_mode_ctx(MODE_EDIT):
        return [
            EditBone.fromBlenderEditBone(bone)
            for bone
            in get_object().data.edit_bones
            if not bone.parent
        ]


def restore_armature_snapshot(snapshot):
    def _recurse_restore(bone):
        if not has_bone(bone.name):
            create_bone(
                bone.name,
                parent_name=bone.parent_name,
                parenting_type=PARENT_TYPE_CONNECTED if bone.connect else PARENT_TYPE_OFFSET
            )
        bone.editbone_restore(get_bone(bone.name))

        for child in bone.children:
            _recurse_restore(child)

    with active_mode_ctx(MODE_EDIT):
        with mirror_x_ctx(False):
            snapshot_bone_names = set()
            for bone in snapshot:
                snapshot_bone_names.update(bone.get_bone_names_recursively())

            for_deletion = [
                bone.name
                for bone
                in get_object().data.edit_bones
                if bone.name not in snapshot_bone_names
            ]

            for bone_name in for_deletion:
                delete_bone(bone_name)

            for bone in snapshot:
                _recurse_restore(bone)
