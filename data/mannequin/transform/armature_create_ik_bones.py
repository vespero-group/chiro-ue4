from ....utils.transform import CallBack
from ....utils import arma, mode


_ARMATURE = None


def get_armature():
    global _ARMATURE
    if _ARMATURE:
        return _ARMATURE

    from ...armature import get

    _ARMATURE = get('mannequin', 'origin')

    return _ARMATURE


def _gen_root_bone(armature, bone_name):
    armature.get_bone(bone_name).editbone_restore(arma.create_bone(bone_name))


def _gen_child_bone(armature, bone_name, parent_name, snap_to_name=None):
    bone = arma.create_bone(bone_name, parent_name)
    armature.get_bone(bone_name).editbone_restore(bone)
    if snap_to_name is not None:
        arma.snap_bone_to_bone(bone_name, snap_to_name)


def _gen_ik_hand_root(armature):
    _gen_root_bone(armature, 'ik_hand_root')
    _gen_child_bone(armature, 'ik_hand_gun', 'ik_hand_root', 'hand_r')
    _gen_child_bone(armature, 'ik_hand_l', 'ik_hand_gun', 'hand_l')
    _gen_child_bone(armature, 'ik_hand_r', 'ik_hand_gun', 'hand_r')


def _gen_ik_foot_root(armature):
    _gen_root_bone(armature, 'ik_foot_root')
    _gen_child_bone(armature, 'ik_foot_l', 'ik_foot_root', 'foot_l')
    _gen_child_bone(armature, 'ik_foot_r', 'ik_foot_root', 'foot_r')


def _run(_):
    with mode.active_mode_ctx(mode.MODE_EDIT):
        with arma.unselect_bones_ctx():
            with arma.mirror_x_ctx(False):
                root = get_armature()
                _gen_ik_foot_root(root)
                _gen_ik_hand_root(root)


_BONES = {
    'ik_hand_root',
    'ik_hand_gun',
    'ik_hand_l',
    'ik_hand_r',
    'ik_foot_root',
    'ik_foot_l',
    'ik_foot_r'
}


def poll(ctx):
    if not ctx or not ctx.object or not ctx.object.type == 'ARMATURE':
        return False

    for bone in _BONES:
        if bone not in ctx.object.data.bones:
            return True

    return False


SCHEMA = {
    'id': 'make-ik-bones',
    'name': 'Make IK bones',
    'description': 'Create the IK bones matching Mannequin armature',
    'poll': poll,
    'actions': [
        # Apply everything
        CallBack(_run),
    ]
}
