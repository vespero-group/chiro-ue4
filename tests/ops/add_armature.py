import bpy

from ...data import armature
from ..test_mixin import TestMixin


class TestAddArmature(TestMixin):
    "Test adding armature to the scene"

    bl_idname = "chiro_ue4.test_op_add_armature"
    bl_label = "Test | Add armature"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        assert 'root' not in bpy.data.objects

        self.log('Polling the operator ...')
        assert bpy.ops.chiro_ue4.op_add_armature.poll()
        self.log('Polling the operator ... SUCCESS')

        self._run_option()

        for option in armature.get_options_generator()(self):
            self._run_option(option)

    def _run_option(self, option=None):
        self.log("Calling the operator with option '{}' ...".format(option if option else 'Default'))

        with self.notice_created_objects() as keys:
            if option:
                bpy.ops.chiro_ue4.op_add_armature(armature_option=option[0])
            else:
                bpy.ops.chiro_ue4.op_add_armature()

        assert len(keys) == 1
        assert list(keys)[0] == 'root'
        assert bpy.data.objects['root'].type == 'ARMATURE'

        self.log('Calling the operator ... SUCCESS')

        bpy.data.objects.remove(bpy.data.objects['root'])
