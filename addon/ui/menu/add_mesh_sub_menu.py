import bpy

from ...ops import AddMesh
from ...data import mesh


class AddMeshSubMenu(bpy.types.Menu):
    """The submenu for Add-Mesh section"""

    bl_idname = "CHIRO_UE4_MANNEQUIN_MT_add_mesh_submenu"
    bl_label = "Chiro (UE4 Mannequin)"

    def draw(self, ctx):
        layout = self.layout
        layout.label(text=self.bl_label)

        layout.operator(AddMesh.bl_idname, text="T-Pose").mesh_option = \
            mesh.gen_option_key('mannequin', 'pose-t')

        layout.operator(AddMesh.bl_idname, text="A-Pose").mesh_option = \
            mesh.gen_option_key('mannequin', 'pose-a')

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
