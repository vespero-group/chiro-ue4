"""UIs provided by the addon

User interface components implementation
"""


from .panels import (
    EXPORT as EXPORT_PANELS,
    register as register_panels,
    unregister as unregister_panels,
)

from .menu import (
    EXPORT as EXPORT_MENU,
    register as register_menu,
    unregister as unregister_menu
)

EXPORT = []
EXPORT.extend(EXPORT_PANELS)
EXPORT.extend(EXPORT_MENU)


def register():
    register_menu()
    register_panels()


def unregister():
    unregister_panels()
    unregister_menu()
