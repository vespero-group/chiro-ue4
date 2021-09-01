import bpy

from .operator_mixin import OperatorMixin
from ..utils import context, mode, object, export_helper
from .. import data


class FbxExport(OperatorMixin):
    "Export in FBX format"

    bl_idname = "chiro_ue4.export_fbx"
    bl_label = "Export FBX (Chiro UE4)"

    save_path: bpy.props.EnumProperty(name='Save as', items=export_helper.get_gen_options_callback('fbx'))

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        if cls.poll(ctx):
            box = layout.box()
            box.label(text="Export FBX")
            box.prop(ctx.object, 'name', text='Target')
            box.operator_menu_enum(cls.bl_idname, "save_path")

    @classmethod
    def poll(cls, ctx):
        return ctx \
            and ctx.object \
            and ctx.object.type == "ARMATURE" \
            and bool(bpy.data.filepath)

    def _run(self):
        self._export_into(self.save_path)

    def _select_recursive(self, obj, select, select_everything):
        for child in obj.children:
            if child.type == 'EMPTY':
                if select_everything:
                    child.select_set(select)
                self._select_recursive(child, select, select_everything)
            else:
                child.select_set(select)

    def _export_into(self, path):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with context.active_object_ctx(context.get_object().name):
                obj = context.get_active_object()
                self._select_recursive(context.get_active_object(), True, True)
                bpy.ops.object.duplicate_move()

                self._select_recursive(context.get_active_object(), False, True)
                renamedRootIndex = 0

                with context.active_object_ctx(context.get_object().name):
                    with object.location_applied_ctx():
                        with object.rotation_applied_ctx():
                            with object.scale_applied_ctx(1):
                                bpy.ops.chiro_ue4.op_transform(transform=data.transform.gen_option_key('mannequin', 'chiropract'))
                                bpy.ops.chiro_ue4.op_transform(transform=data.transform.gen_option_key('mannequin', 'make-ik-bones'))

                            # select the child meshes
                            self._select_recursive(context.get_active_object(), True, False)

                            # select the armature
                            context.get_active_object().select_set(True)

                            if context.get_active_object().name != 'root':
                                renamedRootIndex = 1 # default to 1
                                if 'root' in bpy.data.objects:
                                    while 'root.' + str(renamedRootIndex).zfill(3) in bpy.data.objects:
                                        renamedRootIndex += 1
                                    bpy.data.objects['root'].name = 'root.' + str(renamedRootIndex).zfill(3)
                                context.get_active_object().name = 'root'

                            with object.scale_applied_ctx(0.01):
                                bpy.ops.export_scene.fbx(
                                    filepath=path,
                                    check_existing=False,
                                    use_active_collection=True,
                                    use_selection=True,
                                    global_scale=1,
                                    apply_scale_options='FBX_SCALE_NONE',
                                    object_types={'ARMATURE', 'MESH'},
                                    use_mesh_modifiers=False,
                                    mesh_smooth_type='FACE',
                                    add_leaf_bones=False,
                                    primary_bone_axis='X',
                                    secondary_bone_axis='Y',
                                    armature_nodetype='ROOT',
                                    bake_anim=False,
                                    path_mode='COPY',
                                    embed_textures=True
                                )

                # select all children of duplicated armature, regardless if mesh
                self._select_recursive(context.get_active_object(), True, True)

                bpy.ops.object.delete(use_global=True, confirm=False)

                if renamedRootIndex > 0:
                    bpy.data.objects['root.' + str(renamedRootIndex).zfill(3)].name = 'root'
