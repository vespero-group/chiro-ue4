"""Mode utilities

Utility functions for working with Blender modes
"""


import bpy
from contextlib import contextmanager
from .context import get as get_context, get_object


MODE_OBJECT = "OBJECT"
MODE_EDIT = "EDIT"
MODE_POSE = "POSE"
MODE_SCULPT = "SCULPT"
MODE_VERTEX_PAINT = "VERTEX_PAINT"
MODE_WEIGHT_PAINT = "WEIGHT_PAINT"
MODE_TEXTURE_PAINT = "TEXTURE_PAINT"
MODE_PARTICLE_EDIT = "PARTICLE_EDIT"
MODE_EDIT_GPENCIL = "EDIT_GPENCIL"
MODE_SCULPT_GPENCIL = "SCULPT_GPENCIL"
MODE_PAINT_GPENCIL = "PAINT_GPENCIL"
MODE_VERTEX_GPENCIL = "VERTEX_GPENCIL"
MODE_WEIGHT_GPENCIL = "WEIGHT_GPENCIL"


@contextmanager
def active_mode_ctx(mode):
    if not get_object():
        if mode == get_context().mode:
            yield
            return
        else:
            raise Exception('The context object is not set')

    current_mode = get_object().mode

    try:
        switch_mode(mode)
        yield

    finally:
        switch_mode(current_mode)


def switch_mode(mode):
    try:
        bpy.ops.object.mode_set(mode=mode)
    except Exception:
        bpy.ops.object.mode_set(mode=MODE_OBJECT)
