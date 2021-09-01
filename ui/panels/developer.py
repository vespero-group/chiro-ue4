from bpy.types import Panel
from ...ops import FbxExport
from ...ops.dev.export_armature import ExportArmature
from ...ops.dev.export_mesh import ExportMesh
from ...utils.cfg import is_developer_mode

from ...tests import (
    TestAddArmature, TestAddMesh, TestAddSkeletalMesh, TestApplyPoseToMesh,
    TestFbxExport, TestRePose, TestSelectBoneGroup, TestTransform
)


class DeveloperPanel(Panel):
    """Chiro UE4 Export Panel"""

    bl_category = "Chiro (UE4 Mannequin)"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bl_label = "Chiro UE4 Developer Panel"
    bl_idname = "CHIRO_UE4_MANNEQUIN_PT_DeveloperPanel"

    @classmethod
    def poll(cls, ctx):
        return is_developer_mode()

    def draw(self, ctx):
        FbxExport.draw_in_layout(ctx, self.layout)
        ExportArmature.draw_in_layout(ctx, self.layout)
        ExportMesh.draw_in_layout(ctx, self.layout)

        TestAddArmature.draw_in_layout(ctx, self.layout)
        TestAddMesh.draw_in_layout(ctx, self.layout)
        TestAddSkeletalMesh.draw_in_layout(ctx, self.layout)
        TestApplyPoseToMesh.draw_in_layout(ctx, self.layout)
        TestFbxExport.draw_in_layout(ctx, self.layout)
        TestRePose.draw_in_layout(ctx, self.layout)
        TestSelectBoneGroup.draw_in_layout(ctx, self.layout)
        TestTransform.draw_in_layout(ctx, self.layout)
