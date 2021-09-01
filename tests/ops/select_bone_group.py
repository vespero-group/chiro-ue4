import bpy

from ...ops import select_bone_group
from ...utils import arma, context, mode
from ..test_mixin import TestMixin


class TestSelectBoneGroup(TestMixin):
    "Test select bone group"

    bl_idname = "chiro_ue4.test_op_select_bone_group"
    bl_label = "Test | Select Bone Group"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_key, mesh_key = self._prepare_the_stage()

        with context.active_object_ctx(armature_key):
            with mode.active_mode_ctx(mode.MODE_EDIT):
                with arma.selected_bones_ctx([]):
                    assert not len(context.get().selected_editable_bones)

                    def the_filter(a, g, v):
                        return a == 'mannequin' and g == 'twist' and v == 'all'

                    option_key = select_bone_group._get_bg_options_generator(
                        filter=the_filter
                    )(self)[0][0]

                    bpy.ops.chiro_ue4.op_select_bone_group(bone_group_option_key=option_key)

                    assert len(context.get().selected_editable_bones) == 8

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
