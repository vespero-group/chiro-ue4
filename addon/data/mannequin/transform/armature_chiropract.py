from ....utils.transform import CallBack
from ....utils import arma, mode
from mathutils import Vector


_ARMATURE = None


def get_armature():
    global _ARMATURE
    if _ARMATURE:
        return _ARMATURE

    from ...armature import get

    _ARMATURE = get('mannequin', 'origin')

    return _ARMATURE


def _update_bone(bone, parent=None):
    if not arma.has_bone(bone.name):
        return

    edit_bone = arma.get_bone(bone.name)

    rel_tail = Vector(bone.tail) - Vector(bone.head)

    edit_bone.tail = edit_bone.head + rel_tail
    edit_bone.roll = bone.roll


def _update_bones():
    root = get_armature()
    root.recursively(lambda b, _: arma.disconnect_children(b.name) if arma.has_bone(b.name) else None)
    root.recursively(_update_bone)


def _run(_):
    with mode.active_mode_ctx(mode.MODE_EDIT):
        with arma.unselect_bones_ctx():
            with arma.mirror_x_ctx(False):
                _update_bones()


def poll(ctx):
    if not ctx or not ctx.object or not ctx.object.type == 'ARMATURE':
        return False

    return True


SCHEMA = {
    'id': 'chiropract',
    'name': 'Chiropract on Armature',
    'description': 'Chiropract on Armature to make it UE4 Mannequin compatible',
    'poll': poll,
    'actions': [
        # Apply everything
        CallBack(_run),
    ]
}
