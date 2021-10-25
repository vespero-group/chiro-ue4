from mathutils import Matrix
from ....utils.transform import CallBack, ReRoll
from ....utils import arma, context, mode, object


spine_mtx = Matrix(((-4.371138828673793e-08, 0.0, 1.0, 0.0), (1.0, 0.0, 4.371138828673793e-08, 0.0), (0.0, 0.9999999403953552, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
arm_l_mtx = Matrix(((0.0, 1.0, 0.0, 0.0), (1.0, 0.0, 8.742277657347586e-08, 0.0), (8.742277657347586e-08, 0.0, -1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
hand_l_mtx = Matrix(((0.0, 0.9999999403953552, 0.0, 0.0), (4.371138828673793e-08, 0.0, -1.0, 0.0), (-1.0, 0.0, -4.371138828673793e-08, 0.0), (0.0, 0.0, 0.0, 1.0)))
thumb_l_mtx = Matrix(((0.7071067690849304, 0.7071066498756409, 6.181723932741079e-08, 0.0), (0.7071065902709961, -0.7071066498756409, 6.181723932741079e-08, 0.0), (8.742276236262114e-08, 0.0, -1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
leg_l_mtx = Matrix(((-4.371138828673793e-08, 0.0, -1.0, 0.0), (1.0, 0.0, -4.371138828673793e-08, 0.0), (0.0, -0.9999999403953552, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
foot_l_mtx = Matrix(((-4.371138828673793e-08, 0.0, -0.9999998211860657, 0.0), (0.7071067690849304, -0.7071067094802856, 8.940696716308594e-08, 0.0), (-0.7071067690849304, -0.7071067094802856, 8.940696716308594e-08, 0.0), (0.0, 0.0, 0.0, 1.0)))
ball_l_mtx = Matrix(((0.9999939203262329, 0.0, 0.0034905283246189356, 0.0), (0.0, -1.0, 0.0, 0.0), (0.0034905283246189356, 0.0, -0.9999939203262329, 0.0), (0.0, 0.0, 0.0, 1.0)))

arm_r_mtx = Matrix(((0.0, -1.0, 0.0, 0.0), (-1.0, 0.0, -8.742277657347586e-08, 0.0), (8.742277657347586e-08, 0.0, -1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
hand_r_mtx = Matrix(((0.0, -0.9999999403953552, 0.0, 0.0), (-4.371138828673793e-08, 0.0, -1.0, 0.0), (1.0, 0.0, -4.371138828673793e-08, 0.0), (0.0, 0.0, 0.0, 1.0)))
thumb_r_mtx = Matrix(((0.7071066498756409, -0.7071071267127991, 6.181722511655607e-08, 0.0), (-0.7071073651313782, -0.7071068286895752, -6.181726064369286e-08, 0.0), (8.742281210061265e-08, -3.552713678800501e-15, -1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
leg_r_mtx = Matrix(((-4.371138828673793e-08, 0.0, 1.0, 0.0), (-1.0, 0.0, -4.371138828673793e-08, 0.0), (0.0, -0.9999999403953552, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0)))
foot_r_mtx = Matrix(((-4.371138828673793e-08, 0.0, 1.0000004768371582, 0.0), (-0.7071068286895752, -0.7071068286895752, -2.682209014892578e-07, 0.0), (0.7071068286895752, -0.7071068286895752, -2.086162567138672e-07, 0.0), (0.0, 0.0, 0.0, 1.0)))
ball_r_mtx = ball_l_mtx


SCHEMA = {
    'id': 'bone-roll-t',
    'name': 'Bone Roll T-Pose',
    'description': 'Reroll every bone to match Mannequin armature in T-Pose',
    'actions':
        [ReRoll(bone, spine_mtx) for bone in (
            'pelvis', 'spine_01', 'spine_02',
            'spine_03', 'neck_01', 'head')]

        + [ReRoll(bone, arm_l_mtx) for bone in (
            'clavicle_l', 'upperarm_l',
            'upperarm_twist_01_l', 'lowerarm_l',
            'lowerarm_twist_01_l')]
        + [ReRoll(bone, hand_l_mtx) for bone in (
            'hand_l',
            'index_01_l', 'index_02_l', 'index_03_l',
            'middle_01_l', 'middle_02_l', 'middle_03_l',
            'ring_01_l', 'ring_02_l', 'ring_03_l',
            'pinky_01_l', 'pinky_02_l', 'pinky_03_l',
        )]
        + [ReRoll(bone, thumb_l_mtx)
            for bone
            in ('thumb_01_l', 'thumb_02_l', 'thumb_03_l')]
        + [ReRoll(bone, leg_l_mtx)
            for bone
            in ('thigh_l', 'thigh_twist_01_l', 'calf_l', 'calf_twist_01_l')]
        + [ReRoll('foot_l', foot_l_mtx), ReRoll('ball_l', ball_l_mtx)]

        + [ReRoll(bone, arm_r_mtx) for bone in (
            'clavicle_r', 'upperarm_r',
            'upperarm_twist_01_r', 'lowerarm_r',
            'lowerarm_twist_01_r')]

        + [ReRoll(bone, hand_r_mtx) for bone in (
            'hand_r',
            'index_01_r', 'index_02_r', 'index_03_r',
            'middle_01_r', 'middle_02_r', 'middle_03_r',
            'ring_01_r', 'ring_02_r', 'ring_03_r',
            'pinky_01_r', 'pinky_02_r', 'pinky_03_r',
        )]
        + [ReRoll(bone, thumb_r_mtx)
            for bone
            in ('thumb_01_r', 'thumb_02_r', 'thumb_03_r')]
        + [ReRoll(bone, leg_r_mtx)
            for bone
            in ('thigh_r', 'thigh_twist_01_r', 'calf_r', 'calf_twist_01_r')]
        + [ReRoll('foot_r', foot_r_mtx), ReRoll('ball_r', ball_r_mtx)]
}
