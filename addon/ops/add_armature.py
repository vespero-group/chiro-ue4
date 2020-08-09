import bpy

from ..data import armature

from .operator_mixin import OperatorMixin
from ..utils import arma, context, mode


class AddArmature(OperatorMixin):
    "Add armature to the scene"

    bl_idname = "chiro_ue4.op_add_armature"
    bl_label = "Add armature"

    armature_option: bpy.props.EnumProperty(items=armature.get_options_generator(), name='Armature')

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        self._create_armature()

    def _create_armature(self):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            # Add armature object
            bpy.ops.object.armature_add()
            obj = context.get().active_object
            obj.name = "root"
            obj.data.name = "root"

        with mode.active_mode_ctx(mode.MODE_EDIT):
            # Remove default bone
            bones = context.get().active_object.data.edit_bones
            bones.remove(bones[0])
            # Create the bones
            self._create_bones(armature.get_by_option_key(self.armature_option))

    def _create_bones(self, root):
        with arma.mirror_x_ctx(False):
            for bone in root.children:
                bone.recursively(self._build_bone)

    @classmethod
    def _build_bone(cls, bone, parent=None):
        parent_name = parent.name if parent else None
        bone.editbone_restore(arma.create_bone(bone.name, parent_name))
