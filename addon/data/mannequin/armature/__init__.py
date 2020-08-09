from . import bone_group, origin, corrected_pose_a, corrected_pose_t


SCHEMA = {
    'id': 'mannequin',
    'name': 'Mannequin',
    'variants': [
        origin.SCHEMA,
        corrected_pose_a.SCHEMA,
        corrected_pose_t.SCHEMA
    ],
    'bone_groups': bone_group.GROUPS
}
