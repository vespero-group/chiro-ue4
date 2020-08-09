import bpy

from ..data import armature, mesh
from ..utils import context, mode
from .operator_mixin import OperatorMixin


def get_options_generator(filter=None, arma_filter=None, mesh_filter=None):
    def _options(self, ctx=None):
        result = []

        armature_options = armature.get_options_generator(arma_filter)(self, ctx)
        mesh_options = mesh.get_options_generator(mesh_filter)(self, ctx)

        for a_opt in armature_options:
            a_model_key, a_variant_key = list(map(int, a_opt[0].split(':')))

            for m_opt in mesh_options:
                m_model_key, m_variant_key = list(map(int, m_opt[0].split(':')))

                a_model = armature.ARMATURES[a_model_key]
                m_model = mesh.MESHES[m_model_key]

                if a_model['id'] != m_model['id']:
                    # models don't match
                    continue

                a_variant = a_model['variants'][a_variant_key]
                m_variant = m_model['variants'][m_variant_key]

                if a_variant['id'] != m_variant['id']:
                    # variants don't match
                    continue

                if (filter
                        and not filter(
                            (a_model['id'], a_variant['id']),
                            (m_model['id'], m_variant['id'])
                        )):
                    continue

                option_key = '{}+{}'.format(a_opt[0], m_opt[0])
                option_name = '{} --> {}'.format(m_model['name'], m_variant['name'])

                result.append((option_key, option_name, ""))

        return result
    return _options


class AddSkeletalMesh(OperatorMixin):
    "Add Skeletal Mesh to the scene"

    bl_idname = "chiro_ue4.op_add_skeletal_mesh"
    bl_label = "Add Skeletal Mesh"

    the_option: bpy.props.EnumProperty(items=get_options_generator(), name='Skeletal Mesh')

    @classmethod
    def poll(cls, ctx):
        return True

    def _run(self):
        armature_option, mesh_option = self.the_option.split('+')

        with mode.active_mode_ctx(mode.MODE_OBJECT):
            objects_before = set(o.name for o in bpy.data.objects)
            bpy.ops.chiro_ue4.op_add_mesh(mesh_option=mesh_option)
            objects_after = set(o.name for o in bpy.data.objects)
            mesh_name = objects_after.difference(objects_before).pop()

            objects_before = set(o.name for o in bpy.data.objects)
            bpy.ops.chiro_ue4.op_add_armature(armature_option=armature_option)
            objects_after = set(o.name for o in bpy.data.objects)
            armature_name = objects_after.difference(objects_before).pop()

            mesh_obj = bpy.data.objects[mesh_name]
            arma_obj = bpy.data.objects[armature_name]
            with context.selected_objects_ctx((mesh_obj, arma_obj)):
                with context.active_object_ctx(armature_name):
                    bpy.ops.object.parent_set(type='ARMATURE_NAME')
