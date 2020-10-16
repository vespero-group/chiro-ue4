import bpy
from contextlib import contextmanager
from ..utils import context


class TestMixin(bpy.types.Operator):
    bl_options = {'REGISTER'}

    class ReturnSuccess(Exception):
        pass

    class ReturnFailure(Exception):
        pass

    @classmethod
    def get_menu_func(cls, icon="OUTLINER_OB_ARMATURE"):
        def menu_item(self, ctx):
            self.layout.operator(cls.bl_idname, text=cls.bl_label, icon=icon)

        return menu_item

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        if cls.poll(ctx):
            box = layout.box()
            box.label(text=cls.bl_label)
            box.operator(cls.bl_idname, text=cls.bl_label, icon="OUTLINER_OB_ARMATURE")

    def execute(self, ctx):
        self.log("Executing {}".format(type(self).__name__))
        try:
            with context.with_blender_context(ctx):
                self._run()
        except self.ReturnSuccess:
            pass
        except self.ReturnFailure:
            return {"CANCELLED"}

        return {"FINISHED"}

    def log(self, msg, level={"INFO"}):
        self.report(level, '{} | {}'.format(self.bl_label, msg))

    @contextmanager
    def notice_created_objects(self):
        register = set()

        before = set(list(bpy.data.objects.keys()))
        yield register
        after = set(list(bpy.data.objects.keys()))

        register.update(after.difference(before))

    def _find_group_vertices(self, mesh, group_name):
        group_idx = mesh.vertex_groups[group_name].index
        return [vtx for vtx in mesh.data.vertices if group_idx in [g.group for g in vtx.groups]]
