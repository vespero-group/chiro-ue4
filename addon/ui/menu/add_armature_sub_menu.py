import bpy

from ...ops import AddArmature, Transform
from ...data import armature, transform
from ...utils.cfg import is_advanced_mode


class AddArmatureSubMenu(bpy.types.Menu):
    """The submenu for Add-Armature section"""

    bl_idname = "CHIRO_UE4_MANNEQUIN_MT_add_mannequin_armature_submenu"
    bl_label = "Chiro (UE4 Mannequin)"

    def draw(self, ctx):
        layout = self.layout
        layout.label(text=self.bl_label)

        layout.operator(AddArmature.bl_idname, text="T-Pose").armature_option = \
            armature.gen_option_key('mannequin', 'pose-t')

        layout.operator(AddArmature.bl_idname, text="A-Pose").armature_option = \
            armature.gen_option_key('mannequin', 'pose-a')

        layout.separator()

        layout.operator(Transform.bl_idname, text="Twist Bones").transform = \
            transform.gen_option_key('mannequin', 'make-twist-bones')

        if is_advanced_mode():
            layout.operator(Transform.bl_idname, text="IK Bones").transform = \
                transform.gen_option_key('mannequin', 'make-ik-bones')

            layout.operator(AddArmature.bl_idname, text="The Origin").armature_option = \
                armature.gen_option_key('mannequin', 'origin')

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
