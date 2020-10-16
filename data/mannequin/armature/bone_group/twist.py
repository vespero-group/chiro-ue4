_BONES = [
    'upperarm_twist_01_r',
    'lowerarm_twist_01_r',

    'upperarm_twist_01_l',
    'lowerarm_twist_01_l',

    'thigh_twist_01_r',
    'calf_twist_01_r',

    'thigh_twist_01_l',
    'calf_twist_01_l',
]

SCHEMA = {
    'id': 'twist',
    'name': 'Twist Bones',
    'variants': [
        {
            'id': 'all',
            'name': 'All',
            'bone_names': _BONES
        },

        # {
        #     'id': 'legs',
        #     'name': 'Legs',
        #     'bone_names': list(filter(lambda b: b.find('arm') < 0, _BONES))
        # },

        # {
        #     'id': 'arms',
        #     'name': 'Arms',
        #     'bone_names': list(filter(lambda b: b.find('arm') > -1, _BONES))
        # },

        # {
        #     'id': 'right',
        #     'name': 'Right',
        #     'bone_names': list(filter(lambda b: b.endswith('r'), _BONES))
        # },

        # {
        #     'id': 'left',
        #     'name': 'Left',
        #     'bone_names': list(filter(lambda b: b.endswith('l'), _BONES))
        # },
    ]
}
