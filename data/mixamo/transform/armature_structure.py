from ....utils.transform import Rename, Delete, CallBackRecursively
from ....utils import arma
from ..armature import remove_prefix_callbacks


def _remove_prefix_callback(bone):
    name = remove_prefix_callbacks[0](bone.name)
    arma.get_bone(bone.name).name = name
    return bone.callback(lambda _: name, lambda c: c)


SCHEMA = {
    'id': 'skeleton-convert',
    'name': 'Skeleton conversion',
    'description': 'Rename bones, delete leafs',
    'actions': [
        CallBackRecursively(_remove_prefix_callback),

        Rename({
            'Hips': 'pelvis',
            'Spine': 'spine_01',
            'Spine1': 'spine_02',
            'Spine2': 'spine_03',
            'Neck': 'neck_01',
            'Head': 'head',

            # Left Arm
            'LeftShoulder': 'clavicle_l',
            'LeftArm': 'upperarm_l',
            'LeftForeArm': 'lowerarm_l',
            'LeftHand': 'hand_l',

            'LeftHandThumb1': 'thumb_01_l',
            'LeftHandThumb2': 'thumb_02_l',
            'LeftHandThumb3': 'thumb_03_l',

            'LeftHandIndex1': 'index_01_l',
            'LeftHandIndex2': 'index_02_l',
            'LeftHandIndex3': 'index_03_l',

            'LeftHandMiddle1': 'middle_01_l',
            'LeftHandMiddle2': 'middle_02_l',
            'LeftHandMiddle3': 'middle_03_l',

            'LeftHandRing1': 'ring_01_l',
            'LeftHandRing2': 'ring_02_l',
            'LeftHandRing3': 'ring_03_l',

            'LeftHandPinky1': 'pinky_01_l',
            'LeftHandPinky2': 'pinky_02_l',
            'LeftHandPinky3': 'pinky_03_l',

            # Right Arm
            'RightShoulder': 'clavicle_r',
            'RightArm': 'upperarm_r',
            'RightForeArm': 'lowerarm_r',
            'RightHand': 'hand_r',

            'RightHandThumb1': 'thumb_01_r',
            'RightHandThumb2': 'thumb_02_r',
            'RightHandThumb3': 'thumb_03_r',

            'RightHandIndex1': 'index_01_r',
            'RightHandIndex2': 'index_02_r',
            'RightHandIndex3': 'index_03_r',

            'RightHandMiddle1': 'middle_01_r',
            'RightHandMiddle2': 'middle_02_r',
            'RightHandMiddle3': 'middle_03_r',

            'RightHandRing1': 'ring_01_r',
            'RightHandRing2': 'ring_02_r',
            'RightHandRing3': 'ring_03_r',

            'RightHandPinky1': 'pinky_01_r',
            'RightHandPinky2': 'pinky_02_r',
            'RightHandPinky3': 'pinky_03_r',

            # Left Leg
            'LeftUpLeg': 'thigh_l',
            'LeftLeg': 'calf_l',
            'LeftFoot': 'foot_l',
            'LeftToeBase': 'ball_l',

            # Right Leg
            'RightUpLeg': 'thigh_r',
            'RightLeg': 'calf_r',
            'RightFoot': 'foot_r',
            'RightToeBase': 'ball_r'
        }),

        Delete('HeadTop_End'),
        Delete('LeftHandThumb4'),
        Delete('LeftHandIndex4'),
        Delete('LeftHandMiddle4'),
        Delete('LeftHandRing4'),
        Delete('LeftHandPinky4'),
        Delete('RightHandThumb4'),
        Delete('RightHandIndex4'),
        Delete('RightHandMiddle4'),
        Delete('RightHandRing4'),
        Delete('RightHandPinky4'),
        Delete('LeftToe_End'),
        Delete('RightToe_End')
    ]
}
