from . import armature_structure
from ..armature import HIPS, gen_append_prefix_callback


def poll(ctx):
    if not ctx or not ctx.object:
        return False

    if not ctx.object.data or not ctx.object.data.bones or not len(ctx.object.data.bones):
        return False

    bones = ctx.object.data.bones

    parts = bones[0].name.split(':')

    if len(parts) != 2:
        if bones[0].name == HIPS.name:
            return all((n in bones for n in HIPS.get_bone_names_recursively()))
        return False

    if parts[0] in ['mixamorig', 'mixamorig1', 'mixamorig9']:
        return True


def armature(ctx):
    parts = ctx.object.data.bones[0].name.split(':')
    if len(parts) == 1:
        return HIPS
    return HIPS.callback(*gen_append_prefix_callback(parts[0]))


TRANSFORMS = [
    armature_structure.SCHEMA
]

SCHEMA = {
    'id': 'mixamo',
    'name': 'Mixamo',
    'armature': armature,
    'variants': TRANSFORMS,
    'poll': poll
}
