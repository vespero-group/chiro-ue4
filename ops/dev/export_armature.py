import bpy
import json

from ..operator_mixin import OperatorMixin
from ...utils import context, mode, export_helper
from ...utils.bone import EditBone


class ExportArmature(OperatorMixin):
    '''Export armature to JSON'''

    bl_idname = 'chiro_ue4.op_dev_export_armature'
    bl_label = "(Chiro UE4 Dev) Export armature as JSON"

    save_path: bpy.props.EnumProperty(name='Save as', items=export_helper.get_gen_options_callback('json'))

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        if cls.poll(ctx):
            box = layout.box()
            box.label(text="Export Armature (JSON)")
            box.prop(ctx.object, 'name', text='Target')
            box.operator_menu_enum(cls.bl_idname, "save_path")

    @classmethod
    def poll(cls, ctx):
        '''Checks:
            - mode is armature edit
            - active object is armature
        '''
        return (
            ctx
            and ctx.object
            and ctx.object.type == 'ARMATURE'
        )

    def _run(self):
        with open(self.save_path, 'w+') as f:
            data = self._read_armature()
            json.dump(data, f, separators=(',', ':'))

    def _read_armature(self):
        with mode.active_mode_ctx(mode.MODE_EDIT):
            return [
                EditBone.fromBlenderEditBone(bone).to_tuple()
                for bone
                in context.get_object().data.edit_bones
                if bone.parent is None
            ]
