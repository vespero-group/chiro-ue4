import bpy
from ...ops import SelectBoneGroup


class SelectBoneGroupSubMenu(bpy.types.Menu):
    bl_idname = "CHIRO_UE4_MANNEQUIN_MT_select_bone_group_submenu"
    bl_label = "Select Bone Group (Chiro UE4)"

    def draw(self, ctx):
        SelectBoneGroup.draw_in_layout(ctx, self.layout)

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
