import bpy

from .operator_mixin import OperatorMixin

from ..data import transform as transform_data
from ..utils import arma, context, mode, object, transform


class Transform(OperatorMixin):
    "Apply transformations to armatures and meshes"

    bl_idname = "chiro_ue4.op_transform"
    bl_label = "Transform"

    transform: bpy.props.EnumProperty(items=transform_data.get_options_generator(), name='Transform')

    @classmethod
    def poll(cls, ctx):
        '''Checks:
            - a single editable armature is selected
            - or a single mesh
        '''
        return True \
            and ctx \
            and ctx.object \
            and ctx.object.type in ['ARMATURE']

    @classmethod
    def draw_in_layout(cls, ctx, layout, filter=None):
        transforms_available = transform_data.get_options_generator(filter, ctx)(None)
        if len(transforms_available) > 0:
            for opt in transforms_available:
                model, transform = transform_data.get_by_option_key(opt[0])
                layout.operator(cls.bl_idname, text=opt[1]).transform = opt[0]

    def _run(self):
        with mode.active_mode_ctx(mode.MODE_OBJECT):
            with object.applied_transforms_ctx():
                with mode.active_mode_ctx(mode.MODE_EDIT):
                    with arma.mirror_x_ctx(False):
                        with arma.unselect_bones_ctx():
                            model, transform = transform_data.get_by_option_key(self.transform)

                            if 'poll' in model and not model['poll'](context.get()):
                                raise self.ReturnCancelled()

                            if 'poll' in transform and not transform['poll'](context.get()):
                                raise self.ReturnCancelled()

                            armature = model['armature'](context.get())
                            self._transform(armature, transform['actions'])

    def _transform(self, armature, transforms):
        for action in transforms:
            if isinstance(action, transform.Transform):
                armature = action.transform(armature)

            else:
                raise Exception('Unknown transformation {}'.format(action))
