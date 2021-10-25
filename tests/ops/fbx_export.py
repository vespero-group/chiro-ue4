import bpy
import os
from mathutils import Euler, Vector

from ...utils import context, mesh, mode, pose, fs
from ..test_mixin import TestMixin


class TestFbxExport(TestMixin):
    "Test FBX Export"

    bl_idname = "chiro_ue4.test_op_apply_pose_to_mesh"
    # bl_idname = 'chiro_ue4.CHIRO_UE4_OT_test_op_apply_pose_to_mesh'
    bl_label = "Test | FBX export"

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_key, mesh_key = self._prepare_the_stage()

        self.log('Looking up the arm vertices ...')
        upperarm_vertices = self._get_upperarm_vertices(mesh_key)
        self.log('Looking up the arm vertices ... SUCCESS')

        with fs.temp_file_ctx() as fpath:
            bpy.ops.wm.save_as_mainfile(filepath=fpath)

            fbx_path = '{}.fbx'.format(fpath)

            self.log('Polling the operator ...')
            assert bpy.ops.chiro_ue4.export_fbx.poll()
            self.log('Polling the operator ... SUCCESS')

            self.log('Exporting FBX ...')
            bpy.ops.chiro_ue4.export_fbx()
            assert os.path.exists(fbx_path)
            self.log('Exporting FBX ... SUCCESS')

        try:
            [bpy.data.objects.remove(bpy.data.objects[key]) for key in [armature_key, mesh_key]]

            assert armature_key not in bpy.data.objects
            assert mesh_key not in bpy.data.objects

            assert os.path.getsize(fbx_path) > 1000000  # > 1Mb

            # TODO: import FBX and validate the mesh posture

            # bpy.ops.import_scene.fbx(
            #     filepath=fbx_path,
            #     use_anim=False,
            #     use_subsurf=False
            # )

        finally:
            os.remove(fbx_path)

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
                    vertices = [v.co.to_tuple() for v in self._find_group_vertices(mesh_object, 'upperarm_l')]

        return vertices

