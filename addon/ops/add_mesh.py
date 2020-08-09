import bpy

from ..data import mesh

from .operator_mixin import OperatorMixin


class AddMesh(OperatorMixin):
    "Add Mesh to the scene"

    bl_idname = "chiro_ue4.op_add_mesh"
    bl_label = "Add Mesh"

    mesh_option: bpy.props.EnumProperty(items=mesh.get_options_generator(), name='Mesh')

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        self._create_mesh()

    def _create_mesh(self):
        data_object = mesh.get_by_option_key(self.mesh_option)

        blender_mesh = bpy.data.meshes.new(name=data_object.name)
        blender_mesh.from_pydata(
            vertices=data_object.verts,
            edges=data_object.edges,
            faces=data_object.faces
        )

        blender_object = bpy.data.objects.new(data_object.name, blender_mesh)
        bpy.context.collection.objects.link(blender_object)

        for group_name in data_object.vtx_groups:
            blender_object.vertex_groups.new(name=group_name)

        for vtx_idx in range(0, len(data_object.weight_paint)):
            for group_idx, weight in data_object.weight_paint[vtx_idx]:
                blender_object.vertex_groups[group_idx].add([vtx_idx], weight, 'REPLACE')
