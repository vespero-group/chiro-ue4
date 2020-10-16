import bpy

from .operator_mixin import OperatorMixin
from ..utils import context, mode


class ApplyPoseToMesh(OperatorMixin):
    "Apply the armature pose to its mesh"

    bl_idname = "chiro_ue4.op_apply_pose_to_mesh"
    bl_label = "Apply Pose to Mesh & as Rest"

    @classmethod
    def poll(cls, ctx):
        return (
            ctx.object and ctx.mode == mode.MODE_POSE and ctx.object.type == "ARMATURE"
        )

    def _run(self):
        armature_name = context.get_object().name
        mesh_names = [i.name for i in context.get_object().children if i.type == "MESH"]

        for mesh_name in mesh_names:
            self._apply_armature_modifier(mesh_name, armature_name)

        bpy.ops.pose.armature_apply(selected=False)

    def _get_mesh_modifiers(self, mesh, armature_name, *filters):
        modifiers = []
        for modifier in mesh.modifiers:
            if not isinstance(modifier, bpy.types.ArmatureModifier):
                continue

            if not modifier.object:
                continue

            if modifier.object.name != armature_name:
                continue

            flag = True
            for f in filters:
                if not f(modifier):
                    flag = False
                    break

            if flag:
                modifiers.append(modifier)

        return modifiers

    def _apply_armature_modifier(self, mesh_name, armature_name):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.active_object_ctx(mesh_name):
                mesh = bpy.data.objects[mesh_name]

                modifiers = self._get_mesh_modifiers(mesh, armature_name)
                real_modifier_names = {m.name for m in modifiers}

                for modifier in modifiers:
                    bpy.ops.object.modifier_copy(modifier=modifier.name)

                    the_copy = self._get_mesh_modifiers(
                        mesh,
                        armature_name,
                        lambda m: m.name.startswith(modifier.name + ".")
                        and m.name not in real_modifier_names,
                    )

                    if len(the_copy):
                        bpy.ops.object.modifier_apply(modifier=the_copy[-1].name)
