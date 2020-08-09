from ...utils.bone import Bone


def gen_append_prefix_callback(prefix='mixamorig'):
    return (
        lambda name: '{}:{}'.format(prefix, name),
        lambda bones, *args, **kwargs: [bone.callback(*gen_append_prefix_callback(prefix)) for bone in bones]
    )


append_prefix_callbacks = gen_append_prefix_callback()

remove_prefix_callbacks = (
    lambda name: name.split(':', 1)[1] if name.find(':') > 1 else name,
    lambda bones, *args, **kwargs: [bone.callback(*remove_prefix_callbacks) for bone in bones]
)

_A_SHOULDER = Bone('{side}Shoulder', [
    Bone('{side}Arm', [
        Bone('{side}ForeArm', [
            Bone('{side}Hand', [
                Bone('{side}HandThumb1', [Bone('{side}HandThumb2', [
                     Bone('{side}HandThumb3', [Bone('{side}HandThumb4')])])]),
                Bone('{side}HandIndex1', [Bone('{side}HandIndex2', [
                     Bone('{side}HandIndex3', [Bone('{side}HandIndex4')])])]),
                Bone('{side}HandMiddle1', [Bone('{side}HandMiddle2', [
                     Bone('{side}HandMiddle3', [Bone('{side}HandMiddle4')])])]),
                Bone('{side}HandRing1', [Bone('{side}HandRing2', [
                     Bone('{side}HandRing3', [Bone('{side}HandRing4')])])]),
                Bone('{side}HandPinky1', [Bone('{side}HandPinky2', [
                     Bone('{side}HandPinky3', [Bone('{side}HandPinky4')])])]),
            ])
        ])
    ])
])
_A_LEG = Bone('{side}UpLeg', [
    Bone('{side}Leg', [
        Bone('{side}Foot', [
            Bone('{side}ToeBase', [
                Bone('{side}Toe_End')
            ])
        ])
    ])
])

HIPS = Bone('Hips', [
    Bone('Spine', [
        Bone('Spine1', [
            Bone('Spine2', [
                Bone('Neck', [
                    Bone('Head', [
                        Bone('HeadTop_End')
                    ])
                ]),
                _A_SHOULDER.format(side='Left'),
                _A_SHOULDER.format(side='Right')
            ])
        ])
    ]),
    _A_LEG.format(side='Left'),
    _A_LEG.format(side='Right')
])

ARMATURE = HIPS.callback(*append_prefix_callbacks)
