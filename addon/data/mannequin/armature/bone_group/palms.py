_BONES = [
    'hand_l',

    'thumb_01_l',
    'thumb_02_l',
    'thumb_03_l',

    'index_01_l',
    'index_02_l',
    'index_03_l',

    'middle_01_l',
    'middle_02_l',
    'middle_03_l',

    'ring_01_l',
    'ring_02_l',
    'ring_03_l',

    'pinky_01_l',
    'pinky_02_l',
    'pinky_03_l',

    'hand_r',

    'thumb_01_r',
    'thumb_02_r',
    'thumb_03_r',

    'index_01_r',
    'index_02_r',
    'index_03_r',

    'middle_01_r',
    'middle_02_r',
    'middle_03_r',

    'ring_01_r',
    'ring_02_r',
    'ring_03_r',

    'pinky_01_r',
    'pinky_02_r',
    'pinky_03_r',
]


SCHEMA = {
    'id': 'palm',
    'name': 'Palm',
    'variants': [
        {
            'id': 'all',
            'name': 'All',
            'bone_names': _BONES
        },

        # {
        #     'id': 'fingers',
        #     'name': 'Fingers',
        #     'bone_names': list(filter(lambda b: not b.startswith('hand'), _BONES))
        # },

        # {
        #     'id': 'thumb',
        #     'name': 'Thumb',
        #     'bone_names': list(filter(lambda b: b.startswith('thumb'), _BONES))
        # },

        # {
        #     'id': 'index',
        #     'name': 'Index',
        #     'bone_names': list(filter(lambda b: b.startswith('index'), _BONES))
        # },

        # {
        #     'id': 'middle',
        #     'name': 'Middle',
        #     'bone_names': list(filter(lambda b: b.startswith('middle'), _BONES))
        # },

        # {
        #     'id': 'ring',
        #     'name': 'Ring',
        #     'bone_names': list(filter(lambda b: b.startswith('ring'), _BONES))
        # },

        # {
        #     'id': 'pinky',
        #     'name': 'Pinky',
        #     'bone_names': list(filter(lambda b: b.startswith('pinky'), _BONES))
        # }
    ]
}