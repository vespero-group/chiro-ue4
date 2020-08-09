"""Data

The module contains the data snapshots required by the addon.

MANNEQUIN_JSON: the original armature (with originally inverted bones)
MANNEQUIN_POSE_JSON: the corrected armature (with bones fixed for working in Blender)
"""

from .mannequin import (
    armature as mannequin_armature,
    mesh as mannequin_mesh,
    transform as mannequin_transform
)
from .mixamo import transform as mixamo_transform


ARMATURES = [
    mannequin_armature.SCHEMA
]


MESHES = [
    mannequin_mesh.SCHEMA
]


TRANSFORMS = [
    mixamo_transform.SCHEMA,
    mannequin_transform.SCHEMA
]
