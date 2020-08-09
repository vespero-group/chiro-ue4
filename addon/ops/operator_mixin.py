import bpy
from ..utils import context


class OperatorMixin(bpy.types.Operator):
    bl_options = {'REGISTER', 'UNDO'}

    class ReturnFinished(Exception):
        pass

    class ReturnCancelled(Exception):
        pass

    def execute(self, ctx):
        self.log()
        try:
            with context.with_blender_context(ctx):
                self._run()
        except self.ReturnFinished:
            pass
        except self.ReturnCancelled:
            return {"CANCELLED"}

        return {"FINISHED"}

    def log(self, level={"INFO"}):
        self.report(level, "Execute {}".format(type(self).__name__))

    @classmethod
    def get_menu_func(cls, icon="OUTLINER_OB_ARMATURE"):
        def menu_item(self, ctx):
            self.layout.operator(cls.bl_idname, text=cls.bl_label, icon=icon)

        return menu_item
