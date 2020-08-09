import bpy

from ...ops import fbx_export


class FbxExportSubMenu(bpy.types.Menu):
    """The submenu for Export section"""

    bl_idname = "CHIRO_UE4_MANNEQUIN_MT_fbx_export_submenu"
    bl_label = "FBX (Chiro UE4 Mannequin)"

    def draw(self, ctx):
        layout = self.layout
        layout.label(text=self.bl_label)
        layout.operator_enum(fbx_export.FbxExport.bl_idname, 'save_path')

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
