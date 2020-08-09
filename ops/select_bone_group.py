import bpy

from .operator_mixin import OperatorMixin
from ..data.armature import ARMATURES
from ..utils import arma, context, mode, pose


def _get_bg_options_generator(filter=None):
    def _options(self, ctx=None):
        result = []
        for armature_key in range(0, len(ARMATURES)):
            armature = ARMATURES[armature_key]

            for bone_group_key in range(0, len(armature['bone_groups'])):
                bone_group = armature['bone_groups'][bone_group_key]

                for variant_key in range(0, len(bone_group['variants'])):
                    variant = bone_group['variants'][variant_key]

                    if filter and not filter(armature['id'], bone_group['id'], variant['id']):
                        continue

                    option_key = '{}:{}:{}'.format(armature_key, bone_group_key, variant_key)
                    option_name = '{} --> {}{}'.format(
                        armature['name'],
                        bone_group['name'],
                        ' ({})'.format(variant['name'])
                        if variant['name'] != 'All'
                        else ''
                    )

                    result.append((option_key, option_name, ""))

        return result

    return _options


class SelectBoneGroup(OperatorMixin):
    "Select Bone Group"

    bl_idname = "chiro_ue4.op_select_bone_group"
    bl_label = "Select Bones"

    bone_group_option_key: bpy.props.EnumProperty(items=_get_bg_options_generator())

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        for opt in _get_bg_options_generator()(None):
            layout.operator(cls.bl_idname, text=opt[1]).bone_group_option_key = opt[0]

    @classmethod
    def poll(cls, ctx):
        return (
            ctx
            and ctx.object
            and ctx.object.type == 'ARMATURE'
            and ctx.object.mode in [
                mode.MODE_EDIT,
                mode.MODE_POSE
            ]
        )

    def _run(self):
        obj = context.get_object()

        bones = self.get_bones()

        if obj.mode == mode.MODE_EDIT:
            self._edit_mode(bones)

        elif obj.mode == mode.MODE_POSE:
            self._pose_mode(bones)

    def get_bones(self):
        model_key, bone_group_key, variant_key = list(map(int, self.bone_group_option_key.split(':')))

        return ARMATURES[model_key]['bone_groups'][bone_group_key]['variants'][variant_key]['bone_names']

    def _edit_mode(self, bones):
        arma.select_bones(bones)

    def _pose_mode(self, bones):
        pose.select_bones(bones)
