from ....utils.bone import Bone, EditBone
from ....utils.transform import CallBack
from ....utils import arma


_POSE = None


def get_pose():
    global _POSE
    if _POSE:
        return _POSE

    from ..armature.corrected_pose_t import SCHEMA

    _POSE = Bone('root', [
        EditBone.fromTuple(data)
        for data
        in SCHEMA['load_data']()
    ])

    return _POSE


def create_twist_bone(bone_name):
    if arma.has_bone(bone_name):
        return

    def _recursively(bone, parent=None):
        if bone.name != bone_name:
            return

        la_bone = arma.create_bone(bone_name, parent.name)
        parent = arma.get_bone(parent.name)

        if bone_name.startswith('upperarm'):
            la_bone.head = parent.head.copy()
            la_bone.tail = parent.head + (parent.tail - parent.head) / 2

        else:
            la_bone.head = parent.head + (parent.tail - parent.head) / 2
            la_bone.tail = parent.tail.copy()
            la_bone.length = (bone.tail - bone.head).length
            la_bone.roll = bone.roll

    get_pose().recursively(_recursively)


_BONES = {
    'thigh_twist_01_r',
    'thigh_twist_01_l',
    'calf_twist_01_r',
    'calf_twist_01_l',
    'upperarm_twist_01_r',
    'upperarm_twist_01_l',
    'lowerarm_twist_01_r',
    'lowerarm_twist_01_l'
}


def poll(ctx):
    if not ctx or not ctx.object or not ctx.object.type == 'ARMATURE':
        return False

    for bone in _BONES:
        if bone not in ctx.object.data.bones:
            return True

    return False


SCHEMA = {
    'id': 'make-twist-bones',
    'name': 'Make twist bones',
    'description': 'Create the twist bones matching Mannequin armature',
    'poll': poll,
    'actions': [
        # Apply everything
        CallBack(lambda _: create_twist_bone('thigh_twist_01_r')),
        CallBack(lambda _: create_twist_bone('thigh_twist_01_l')),
        CallBack(lambda _: create_twist_bone('calf_twist_01_r')),
        CallBack(lambda _: create_twist_bone('calf_twist_01_l')),
        CallBack(lambda _: create_twist_bone('upperarm_twist_01_r')),
        CallBack(lambda _: create_twist_bone('upperarm_twist_01_l')),
        CallBack(lambda _: create_twist_bone('lowerarm_twist_01_r')),
        CallBack(lambda _: create_twist_bone('lowerarm_twist_01_l')),
    ]
}
