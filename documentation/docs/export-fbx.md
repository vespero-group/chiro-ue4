# Export FBX

Export to FBX with autocorrection.
Does not change anything in the open blend scene or file.

This operation:

 - corrects the scale (no need to mess with the scene unit scale)
 - corrects the bone rotations so they match the Mannequin origin (aka chiropract)
 - generates IK bones (if they don't exist yet)
 - autocorrects the armature root name ("root" in UE4 skeleton)
 - Exports the result into FBX

File -> Export -> FBX (Chiro UE4 Mannequin) -> Save as ...

!!! WARNING
    You only choose the file name. The folder is of the original blend file

[![Export FBX Menu](img/feature/export-fbx/export-fbx-menu.png)](img/feature/export-fbx/export-fbx-menu.png)


[![Export FBX](img/feature/export-fbx/export-fbx.png)](img/feature/export-fbx/export-fbx.png)
