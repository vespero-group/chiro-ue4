from ....utils import arma
from ....utils.transform import CallBack, SnapToChild


SCHEMA = {
    'id': 'connect-with-children',
    'name': 'Connect the bones with children',
    'description': 'Snap tails to children and connect',
    'actions': [
        # Spine
        SnapToChild('pelvis', 'spine_01'),
        SnapToChild('spine_01', 'spine_02'),
        SnapToChild('spine_02', 'spine_03'),
        SnapToChild('spine_03', 'neck_01'),
        SnapToChild('neck_01', 'head'),

        # Arm L
        SnapToChild('clavicle_l', 'upperarm_l'),
        SnapToChild('upperarm_l', 'lowerarm_l'),
        SnapToChild('lowerarm_l', 'hand_l'),

        # Arm R
        SnapToChild('clavicle_r', 'upperarm_r'),
        SnapToChild('upperarm_r', 'lowerarm_r'),
        SnapToChild('lowerarm_r', 'hand_r'),

        # Palm L
        SnapToChild('thumb_01_l', 'thumb_02_l'),
        SnapToChild('thumb_02_l', 'thumb_03_l'),
        SnapToChild('index_01_l', 'index_02_l'),
        SnapToChild('index_02_l', 'index_03_l'),
        SnapToChild('middle_01_l', 'middle_02_l'),
        SnapToChild('middle_02_l', 'middle_03_l'),
        SnapToChild('ring_01_l', 'ring_02_l'),
        SnapToChild('ring_02_l', 'ring_03_l'),
        SnapToChild('pinky_01_l', 'pinky_02_l'),
        SnapToChild('pinky_02_l', 'pinky_03_l'),

        # Palm R
        SnapToChild('thumb_01_r', 'thumb_02_r'),
        SnapToChild('thumb_02_r', 'thumb_03_r'),
        SnapToChild('index_01_r', 'index_02_r'),
        SnapToChild('index_02_r', 'index_03_r'),
        SnapToChild('middle_01_r', 'middle_02_r'),
        SnapToChild('middle_02_r', 'middle_03_r'),
        SnapToChild('ring_01_r', 'ring_02_r'),
        SnapToChild('ring_02_r', 'ring_03_r'),
        SnapToChild('pinky_01_r', 'pinky_02_r'),
        SnapToChild('pinky_02_r', 'pinky_03_r'),

        # Leg L
        SnapToChild('thigh_l', 'calf_l'),
        SnapToChild('calf_l', 'foot_l'),
        SnapToChild('foot_l', 'ball_l'),

        # Leg R
        SnapToChild('thigh_r', 'calf_r'),
        SnapToChild('calf_r', 'foot_r'),
        SnapToChild('foot_r', 'ball_r')
    ]
}
