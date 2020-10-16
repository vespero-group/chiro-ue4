import bpy

from ...data.transform import gen_option_key
from ...utils import arma, context, mode
from ..test_mixin import TestMixin


class TestTransform(TestMixin):
    "Test Transform"

    bl_idname = "chiro_ue4.test_op_transform"
    bl_label = "Test | Transform"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_key, mesh_key = self._prepare_the_stage()

        with context.active_object_ctx(armature_key):
            with mode.active_mode_ctx(mode.MODE_EDIT):
                with arma.selected_bones_ctx([]):
                    assert not arma.has_bone('ik_hand_root')
                    assert not arma.has_bone('ik_foot_root')

                    option_key = gen_option_key('mannequin', 'make-ik-bones')
                    bpy.ops.chiro_ue4.op_transform(transform=option_key)

                    assert arma.has_bone('ik_hand_root')
                    assert arma.has_bone('ik_foot_root')

        [bpy.data.objects.remove(bpy.data.objects[key]) for key in [armature_key, mesh_key]]

    def _prepare_the_stage(self):
        assert 'root' not in bpy.data.objects
        assert bpy.ops.chiro_ue4.op_add_skeletal_mesh.poll()

        with self.notice_created_objects() as keys:
            bpy.ops.chiro_ue4.op_add_skeletal_mesh()

        assert len(keys) == 2
        assert 'root' in keys
        mesh_key = [k for k in keys if k != 'root'][0]

        return 'root', mesh_key
