import bpy

from ...ops.add_skeletal_mesh import get_options_generator
from ..test_mixin import TestMixin


class TestAddSkeletalMesh(TestMixin):
    "Test adding skeletal mesh to the scene"

    bl_idname = "chiro_ue4.test_op_add_skeletal_mesh"
    bl_label = "Test | Add skeletal mesh"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        assert 'root' not in bpy.data.objects

        self.log('Polling the operator ...')
        assert bpy.ops.chiro_ue4.op_add_skeletal_mesh.poll()
        self.log('Polling the operator ... SUCCESS')

        self._run_option()

        for option in get_options_generator()(self):
            self._run_option(option)

    def _run_option(self, option=None):
        self.log("Calling the operator with option '{}' ...".format(option if option else 'Default'))

        with self.notice_created_objects() as keys:
            if option:
                bpy.ops.chiro_ue4.op_add_skeletal_mesh(the_option=option[0])
            else:
                bpy.ops.chiro_ue4.op_add_skeletal_mesh()

        assert len(keys) == 2
        assert 'root' in keys
        assert bpy.data.objects['root'].type == 'ARMATURE'
        assert len(bpy.data.objects['root'].children) == 1
        assert bpy.data.objects['root'].children[0].type == 'MESH'

        self.log('Calling the operator ... SUCCESS')

        [bpy.data.objects.remove(bpy.data.objects[key]) for key in keys]
