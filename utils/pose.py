"""Pose utilities

Utility functions for working with Blender Pose APIs
"""

from contextlib import contextmanager
from .context import get_object, get_pose


ROTATION_MODE_QUATERNION = 'QUATERNION'
ROTATION_MODE_XYZ = 'XYZ'
ROTATION_MODE_AXIS_ANGLE = 'AXIS_ANGLE'


def has_bone(bone_name):
    return bone_name in get_pose().bones


def get_bone(bone_name):
    return get_pose().bones[bone_name]


def get_rotation_mode(bone_name):
    return get_bone(bone_name).rotation_mode


def set_rotation_mode(bone_name, mode):
    get_bone(bone_name).rotation_mode = mode


def get_rotation_quat(bone_name):
    return get_bone(bone_name).rotation_quaternion


def set_rotation_quat(bone_name, quat):
    get_bone(bone_name).rotation_quaternion = quat


def add_rotation_quat(bone_name, quat):
    set_rotation_quat(bone_name, quat @ get_rotation_quat(bone_name))


def get_world_matrix(bone_name):
    pose_bone = get_pose().bones[bone_name]

    return get_object().convert_space(
        pose_bone=pose_bone, matrix=pose_bone.matrix, from_space="POSE", to_space="WORLD"
    )


def calc_world_matrix(bone_name):
    pose = get_pose().bones[bone_name]

    local = pose.bone.matrix_local
    basis = pose.matrix_basis

    if not pose.parent:
        return local @ basis
    else:
        parent = pose.parent
        parent_local = parent.bone.matrix_local
        return get_world_matrix(parent.name) @ (parent_local.inverted() @ local) @ basis


@contextmanager
def mirror_x_ctx(enabled=True):
    initial_enabled = get_pose().use_mirror_x

    get_pose().use_mirror_x = enabled

    try:
        yield

    finally:
        get_pose().use_mirror_x = initial_enabled


@contextmanager
def with_rotation_mode(bone_name, mode):
    initial_mode = get_rotation_mode(bone_name)

    set_rotation_mode(bone_name, mode)

    try:
        yield

    finally:
        set_rotation_mode(bone_name, initial_mode)


def unselect_bones():
    for pbone in get_object().pose.bones:
        pbone.bone.select = False
        pbone.bone.select_head = False
        pbone.bone.select_tail = False


@contextmanager
def unselect_bones_ctx():
    initially_selected_bones = [
        (bone, bone.bone.select, bone.bone.select_head, bone.bone.select_tail)
        for bone
        in get_object().pose.bones
        if (bone.bone.select or bone.bone.select_head or bone.bone.select_tail)
    ]

    unselect_bones()
    try:
        yield
    finally:
        unselect_bones()
        for bone, select, select_head, select_tail in initially_selected_bones:
            bone.bone.select = select
            bone.bone.select_head = select_head
            bone.bone.select_tail = select_tail


def select_bones(selected_bone_names=None):
    for bone_name in (selected_bone_names if selected_bone_names else []):
        if has_bone(bone_name):
            get_bone(bone_name).bone.select = True


@contextmanager
def selected_bones_ctx(selected_bone_names=None):
    with unselect_bones_ctx():
        select_bones(selected_bone_names)
        yield
