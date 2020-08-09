from ..operator_mixin import OperatorMixin


class TestOperator(OperatorMixin):
    '''TestOperator'''

    bl_idname = 'chiro_ue4.op_dev_test_operator'
    bl_label = "(Chiro UE4 Dev) Test Operator"

    @classmethod
    def poll(cls, ctx):
        return True

    @classmethod
    def draw_in_layout(cls, ctx, layout):
        box = layout.box()
        box.label(text="TEST")
        box.operator(cls.bl_idname)

    def _run(self):
        # put your testing code here
        pass
