import bpy

from ...ops import add_skeletal_mesh, AddSkeletalMesh
# from ...data import mesh


class AddSkeletalMeshSubMenu(bpy.types.Menu):
    """The submenu for Add section"""

    bl_idname = "CHIRO_UE4_MT_add_skeletal_mesh_submenu"
    bl_label = "Chiro (UE4)"

    def draw(self, ctx):
        layout = self.layout
        layout.label(text=self.bl_label)

        for opt in add_skeletal_mesh.get_options_generator()(None, ctx):
            layout.operator(AddSkeletalMesh.bl_idname, text=opt[1]).the_option = opt[0]

    @classmethod
    def get_submenu(cls):
        def submenu_callback(self, ctx):
            self.layout.menu(
                cls.bl_idname,
                icon="OUTLINER_OB_ARMATURE",
                text=cls.bl_label,
            )

        return submenu_callback
