import bpy
from ...ops import RePose


class RePoseSubMenu(bpy.types.Menu):
    bl_idname = "CHIRO_UE4_MANNEQUIN_MT_repose_submenu"
    bl_label = "Re-Pose (Chiro UE4)"

    def draw(self, _ctx):
        layout = self.layout
        layout.operator_enum(RePose.bl_idname, "pose_variant")

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
