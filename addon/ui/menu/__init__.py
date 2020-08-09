"""UI Menus

User interface menu components
"""


import bpy

from .add_armature_sub_menu import AddArmatureSubMenu
from .add_mesh_sub_menu import AddMeshSubMenu
from .add_skeletal_mesh_sub_menu import AddSkeletalMeshSubMenu
from .edit_armature_sub_menu import EditArmatureSubMenu
from .fbx_export_sub_menu import FbxExportSubMenu
from .re_pose_sub_menu import RePoseSubMenu
from .select_bone_group_sub_menu import SelectBoneGroupSubMenu
from ...ops import ApplyPoseToMesh


EXPORT = [
    AddArmatureSubMenu,
    AddMeshSubMenu,
    AddSkeletalMeshSubMenu,
    EditArmatureSubMenu,
    FbxExportSubMenu,
    RePoseSubMenu,
    SelectBoneGroupSubMenu
]

ADD_ARMATURE_SUBMENU_CALLBACK = AddArmatureSubMenu.get_submenu()
ADD_MESH_SUBMENU_CALLBACK = AddMeshSubMenu.get_submenu()
ADD_SKELETAL_MESH_SUBMENU_CALLBACK = AddSkeletalMeshSubMenu.get_submenu()
EDIT_ARMATURE_SUBMENU_CALLBACK = EditArmatureSubMenu.get_submenu()
FBX_EXPORT_SUBMENU_CALLBACK = FbxExportSubMenu.get_submenu()
REPOSE_SUBMENU_CALLBACK = RePoseSubMenu.get_submenu()
SELECT_BONE_GROUP_SUBMENU_CALLBACK = SelectBoneGroupSubMenu.get_submenu()


def APPLY_POSE_TO_MESH_MENU_CALLBACK(self, ctx):
    self.layout.operator(
        ApplyPoseToMesh.bl_idname,
        text=ApplyPoseToMesh.bl_label+" (Chiro)"
    )


def register():
    bpy.types.VIEW3D_MT_armature_add.append(ADD_ARMATURE_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_mesh_add.append(ADD_MESH_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_add.append(ADD_SKELETAL_MESH_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_pose_apply.append(APPLY_POSE_TO_MESH_MENU_CALLBACK)

    bpy.types.TOPBAR_MT_file_export.append(FBX_EXPORT_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_pose.append(REPOSE_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_select_pose.append(SELECT_BONE_GROUP_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_select_edit_armature.append(SELECT_BONE_GROUP_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_edit_armature.append(EDIT_ARMATURE_SUBMENU_CALLBACK)


def unregister():
    bpy.types.VIEW3D_MT_pose.remove(REPOSE_SUBMENU_CALLBACK)

    bpy.types.TOPBAR_MT_file_export.remove(FBX_EXPORT_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_pose_apply.remove(APPLY_POSE_TO_MESH_MENU_CALLBACK)

    bpy.types.VIEW3D_MT_add.remove(ADD_SKELETAL_MESH_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_mesh_add.remove(ADD_MESH_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_armature_add.remove(ADD_ARMATURE_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_select_pose.remove(SELECT_BONE_GROUP_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_select_edit_armature.remove(SELECT_BONE_GROUP_SUBMENU_CALLBACK)

    bpy.types.VIEW3D_MT_edit_armature.remove(EDIT_ARMATURE_SUBMENU_CALLBACK)
