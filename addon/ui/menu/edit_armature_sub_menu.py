import bpy

from ...ops import Transform
from ...utils import cfg


_advanced_mode_transforms = [
    ('mannequin', 'bone-roll-a'),
    ('mannequin', 'make-ik-bones'),
    ('mannequin', 'chiropract')
]


def filter(model_key, variant_key):
    if not cfg.is_advanced_mode():
        return (model_key, variant_key) not in _advanced_mode_transforms

    return True


class EditArmatureSubMenu(bpy.types.Menu):
    """The submenu for Edit-Armature menu"""

    bl_idname = "CHIRO_UE4_MT_edit_armature_submenu"
    bl_label = "Chiro (UE4)"

    def draw(self, ctx):
        layout = self.layout
        layout.label(text=self.bl_label)

        Transform.draw_in_layout(ctx, layout, filter)

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
