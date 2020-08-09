from ....utils import arma, mode
from ....utils.bone import Bone, EditBone
from ....utils.transform import CallBack


_POSE = None


def get_pose():
    global _POSE
    if _POSE:
        return _POSE

    from ..armature.corrected_pose_a import SCHEMA

    _POSE = Bone('root', [
        EditBone.fromTuple(data)
        for data
        in SCHEMA['load_data']()
    ])

    return _POSE


_BONES = {
    'spine_03',
    'clavicle_r',
    'clavicle_l',
}


def poll(ctx):
    if not ctx or not ctx.object or not ctx.object.type == 'ARMATURE':
        return False

    for bone_name in _BONES:
        if bone_name not in ctx.object.data.bones:
            return False

    return True


def _snap_clavicle(bone_name):
    with mode.active_mode_ctx(mode.MODE_EDIT):
        root = get_pose()

        origin_spine = root.get_bone('spine_03')
        origin_spine_len = (origin_spine.tail - origin_spine.head).length
        origin_clavicle = root.get_bone(bone_name)

        origin_clavicle_position = origin_clavicle.head - origin_spine.tail

        current_spine = arma.get_bone('spine_03')
        current_spine_len = (current_spine.tail - current_spine.head).length

        ratio = current_spine_len / origin_spine_len

        current_clavicle = arma.get_bone(bone_name)

        current_clavicle_position = origin_clavicle_position.copy()
        current_clavicle_position.length = current_clavicle_position.length * ratio * 2

        current_clavicle.head = current_spine.tail + current_clavicle_position


SCHEMA = {
    'id': 'snap_clavicles',
    'name': 'Snap clavicles to Mannequin position',
    'description': 'Create the twist bones matching Mannequin armature',
    'poll': poll,
    'actions': [
        # Apply everything
        CallBack(lambda _: _snap_clavicle('clavicle_r')),
        CallBack(lambda _: _snap_clavicle('clavicle_l')),
    ]
}
