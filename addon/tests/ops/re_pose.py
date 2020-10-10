import bpy
from mathutils import Euler, Vector

from ...data import armature
from ...utils import context, mesh, mode, pose
from ..test_mixin import TestMixin


class TestRePose(TestMixin):
    "Test re-pose armature"

    bl_idname = "chiro_ue4.test_re_pose"
    bl_label = "Test | RePose"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_key, mesh_key = self._prepare_the_stage()

        self.log('Looking up the arm vertices ...')
        orig_upperarm_vertices = self._get_upperarm_vertices(mesh_key)
        self.log('Looking up the arm vertices ... SUCCESS')

        with mode.active_mode_ctx(mode.MODE_POSE):
            variant = armature.gen_option_key('mannequin', 'pose-t')
            bpy.ops.chiro_ue4.op_repose_as(pose_variant=variant)

        self.log('Applying the pose to mesh ...')
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.selected_objects_ctx([bpy.data.objects[armature_key]]):
                with mode.active_mode_ctx(mode.MODE_POSE):
                    bpy.ops.chiro_ue4.op_apply_pose_to_mesh()
        self.log('Applying the pose to mesh ... SUCCESS')

        self.log('Looking up the arm vertices ...')
        updated_upperarm_vertices = self._get_upperarm_vertices(mesh_key)
        self.log('Looking up the arm vertices ... SUCCESS')

        assert orig_upperarm_vertices[0] != updated_upperarm_vertices[0]

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

    def _get_upperarm_vertices(self, mesh_key):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.selected_objects_ctx([bpy.data.objects[mesh_key]]):
                with mode.active_mode_ctx(mode.MODE_EDIT):
                    mesh_object = bpy.data.objects[mesh_key]
                    vertices = [list(round(i, 4) for i in v.co.to_tuple()) for v in self._find_group_vertices(mesh_object, 'upperarm_l')]

        return vertices

