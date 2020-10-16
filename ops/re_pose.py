import bpy

from .operator_mixin import OperatorMixin
from ..utils import context, mode, object, pose
from ..data import armature


exclude_pose_variants = [
    ('mannequin', 'origin')
]


class RePose(OperatorMixin):
    "RePose armature"

    bl_idname = "chiro_ue4.op_repose_as"
    bl_label = "RePose armature"

    pose_variant: bpy.props.EnumProperty(items=armature.get_options_generator(lambda m, v: (m, v) not in exclude_pose_variants), name="Pose")

    @classmethod
    def poll(cls, ctx):
        return ctx and ctx.object and ctx.object.type == 'ARMATURE'

    def _run(self):
        self._pose = armature.get_by_option_key(self.pose_variant)

        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with object.applied_transforms_ctx():
                with mode.active_mode_ctx(mode.MODE_POSE):
                    with pose.mirror_x_ctx(False):
                        for bone in self._pose.children:
                            bone.recursively(self._fix_bone)

    def _fix_bone(self, bone, parent=None):
        if not pose.has_bone(bone.name):
            return

        with pose.with_rotation_mode(bone.name, pose.ROTATION_MODE_QUATERNION):
            deltaL, deltaR, _ = self._get_bone_delta(bone)

            pose.add_rotation_quat(bone.name, deltaR)

            # # TODO: This doesn't make sense for some of the use cases.
            # #       Shifting bones in the global space may be correct
            # #       if the mesh has exact same proportions as the original Mannequin,
            # #       however in the real life we may need to calculate the shift
            # #       relatively to the parent bone, depending on its length in
            # #       comparison to the original bone length (keep the length ratio).
            # #       E.g. if the mesh has shorter arms and hands, its fingers should be
            # #       relocated from the hand relatively to the new hand length.
            # #       This is only a theory though. Needs more investigation.
            # pose.get_bone(bone.name).location += deltaL

        context.get().view_layer.update()

    def _get_bone_delta(self, bone):
        current_mtx = pose.get_world_matrix(bone.name)
        expected_mtx = bone.mtx

        delta_mtx = current_mtx.inverted() @ expected_mtx
        loc, rot, sca = delta_mtx.decompose()

        return loc, rot, sca
