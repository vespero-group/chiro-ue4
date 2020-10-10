import bpy
from mathutils import Euler, Vector

from ...utils import context, mesh, mode, pose
from ..test_mixin import TestMixin


class TestApplyPoseToMesh(TestMixin):
    "Test adding skeletal mesh to the scene"

    bl_idname = "chiro_ue4.test_op_apply_pose_to_mesh"
    bl_label = "Test | Apply Pose to Mesh & as Rest"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_key, mesh_key = self._prepare_the_stage()

        self.log('Polling the operator ...')
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.selected_objects_ctx([bpy.data.objects[armature_key]]):
                with mode.active_mode_ctx(mode.MODE_POSE):
                    assert bpy.ops.chiro_ue4.op_apply_pose_to_mesh.poll()
        self.log('Polling the operator ... SUCCESS')

        self.log('Looking up the arm vertices ...')
        orig_upperarm_vertices = self._get_upperarm_vertices(mesh_key)
        self.log('Looking up the arm vertices ... SUCCESS')

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

        # Rotate the arm forward
        with context.selected_objects_ctx([bpy.data.objects['root']]):
            with mode.active_mode_ctx(mode.MODE_POSE):
                with pose.with_rotation_mode('upperarm_l', pose.ROTATION_MODE_XYZ):
                    pose.get_bone('upperarm_l').rotation_euler = Euler(Vector((0, 0, 1)))

        return 'root', mesh_key

    def _get_upperarm_vertices(self, mesh_key):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.selected_objects_ctx([bpy.data.objects[mesh_key]]):
                with mode.active_mode_ctx(mode.MODE_EDIT):
                    mesh_object = bpy.data.objects[mesh_key]
                    vertices = [list(round(i, 4) for i in v.co.to_tuple()) for v in self._find_group_vertices(mesh_object, 'upperarm_l')]

        return vertices

