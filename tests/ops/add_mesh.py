import bpy

from ...data import mesh
from ..test_mixin import TestMixin


class TestAddMesh(TestMixin):
    "Test adding mesh to the scene"

    bl_idname = "chiro_ue4.test_op_add_mesh"
    bl_label = "Test | Add mesh"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        # assert 'root' not in bpy.data.objects

        self.log('Polling the operator ...')
        assert bpy.ops.chiro_ue4.op_add_mesh.poll()
        self.log('Polling the operator ... SUCCESS')

        self._run_option()

        for option in mesh.get_options_generator()(self):
            self._run_option(option)

    def _run_option(self, option=None):
        self.log("Calling the operator with option '{}' ...".format(option if option else 'Default'))

        with self.notice_created_objects() as keys:
            if option:
                bpy.ops.chiro_ue4.op_add_mesh(mesh_option=option[0])
            else:
                bpy.ops.chiro_ue4.op_add_mesh()

        assert len(keys) == 1
        key = list(keys)[0]
        assert bpy.data.objects[key].type == 'MESH'

        self.log('Calling the operator ... SUCCESS')

        bpy.data.objects.remove(bpy.data.objects[key])
