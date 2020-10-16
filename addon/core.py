"""Core module

Provides Blender Addon API methods implementation
"""

import bpy
from .ui import (
    EXPORT as EXPORT_UI,
    register as register_ui,
    unregister as unregister_ui,
)
from .ops import (
    EXPORT as EXPORT_OPS,
    register as register_ops,
    unregister as unregister_ops,
)
from .tests import (
    EXPORT as EXPORT_TESTS,
    register as register_tests,
    unregister as unregister_tests,
)
from .config import Config


_COMPONENTS = [Config]
_COMPONENTS.extend(EXPORT_OPS)
_COMPONENTS.extend(EXPORT_UI)
_COMPONENTS.extend(EXPORT_TESTS)

def register():
    for component in _COMPONENTS:
        bpy.utils.register_class(component)

    register_ops()
    register_ui()
    register_tests()


def unregister():
    for component in _COMPONENTS[::-1]:
        bpy.utils.unregister_class(component)

    unregister_ui()
    unregister_ops()
    unregister_tests()
