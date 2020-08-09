import bpy
import json
import lzma

from ..operator_mixin import OperatorMixin
from ...utils import mode, object, export_helper, mesh


class ExportMesh(OperatorMixin):
    '''Export mesh'''

    bl_idname = 'chiro_ue4.op_dev_export_mesh'
    bl_label = "(Chiro UE4 Dev) Export mesh (Chiro 1 format)"

    save_path: bpy.props.EnumProperty(name='Save as', items=export_helper.get_gen_options_callback('chrom1xz'))

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        if cls.poll(ctx):
            box = layout.box()
            box.label(text="Export Mesh (Chiro)")
            box.prop(ctx.object, 'name', text='Target')
            box.operator_menu_enum(cls.bl_idname, "save_path")

    @classmethod
    def poll(cls, ctx):
        return (
            ctx
            and ctx.object
            and ctx.object.type == 'MESH'
        )

    def _run(self):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with object.applied_transforms_ctx():
                data = mesh.extract_mesh().to_tuple()

                with lzma.open(self.save_path, mode='w') as fd:
                    fd.write(json.dumps(data, separators=(',', ':')).encode('utf8'))
