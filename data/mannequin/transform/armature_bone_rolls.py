from ....utils.transform import CallBack, CallBackRecursively
from ....utils import arma, mode, object


def reset_bone_rolls(bone):
    from ... import MANNEQUIN_POSE

    if bone.name in MANNEQUIN_POSE and arma.has_bone(bone.name):
        b = arma.get_bone(bone.name)
        b.roll = MANNEQUIN_POSE[bone.name]['roll']


_reset_roll_bones_action = CallBackRecursively(reset_bone_rolls)


def the_callback(armature):
    with mode.active_mode_ctx(mode.MODE_OBJECT):
        with object.applied_transforms_ctx():
            with mode.active_mode_ctx(mode.MODE_EDIT):
                _reset_roll_bones_action.transform(armature)


SCHEMA = {
    'id': 'bone-roll-a',
    'name': 'Bone Roll A-Pose',
    'description': 'Reroll every bone to match Mannequin armature in A-Pose',
    'actions': [
        # Apply everything
        CallBack(the_callback)
    ]
}
