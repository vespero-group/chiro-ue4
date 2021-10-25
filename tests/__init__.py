"""Tests

Auto-tests implementation
"""

from .ops.add_armature import TestAddArmature
from .ops.add_mesh import TestAddMesh
from .ops.add_skeletal_mesh import TestAddSkeletalMesh
from .ops.apply_pose_to_mesh import TestApplyPoseToMesh
from .ops.fbx_export import TestFbxExport
from .ops.re_pose import TestRePose
from .ops.select_bone_group import TestSelectBoneGroup
from .ops.transform import TestTransform

from ..utils import context

EXPORT = [
    TestAddArmature, TestAddMesh, TestAddSkeletalMesh, TestApplyPoseToMesh,
    TestFbxExport, TestRePose, TestSelectBoneGroup, TestTransform
]


def register():
    pass


def unregister():
    pass
