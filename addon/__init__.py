"""Chiro (UE4 Mannequin) for Blender

Tools for skinning with
Unreal Engine 4 Mannequin compatible armature
"""

from .core import register, unregister


bl_info = {
    "name": "Chiro (UE4 Mannequin)",
    "description": "Skinning with Unreal Engine 4 Mannequin armature",
    "author": "Vespero Group (Serge)",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "wiki_url": "https://vespero-group.github.io/chiro-ue4",
    "tracker_url": "https://github.com/vespero-group/chiro-ue4",
    "support": "COMMUNITY",
    "category": "Rigging",
}

if __name__ == "__main__":
    register()
