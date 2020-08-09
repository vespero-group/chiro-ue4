from . import (
    armature_bone_rolls,
    armature_chiropract,
    armature_create_ik_bones,
    armature_create_twist_bones,
    armature_bone_roll_tpose,
    connect_with_children,
    snap_clavicles
)


TRANSFORMS = [
    connect_with_children.SCHEMA,
    snap_clavicles.SCHEMA,
    armature_create_twist_bones.SCHEMA,
    armature_bone_roll_tpose.SCHEMA,
    armature_bone_rolls.SCHEMA,
    armature_create_ik_bones.SCHEMA,
    armature_chiropract.SCHEMA,
]

_ARMATURE = None


def poll(ctx):
    if not ctx or not ctx.object:
        return False

    if not ctx.object.data or not ctx.object.data.bones or not len(ctx.object.data.bones):
        return False

    return 'pelvis' in ctx.object.data.bones


def _load_armature():
    global _ARMATURE

    if _ARMATURE:
        return _ARMATURE

    from ... import armature
    _ARMATURE = armature.get('mannequin', 'origin')

    return _ARMATURE


SCHEMA = {
    'id': 'mannequin',
    'name': 'Mannequin',
    'armature': lambda _: _load_armature(),
    'variants': TRANSFORMS,
    'poll': poll
}
