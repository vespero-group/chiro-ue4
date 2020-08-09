import bmesh
from . import mode, context


class Mesh:
    __slots__ = 'name', 'verts', 'edges', 'faces', 'vtx_groups', 'weight_paint'

    def __init__(self, name, vertices, edges, faces, vtx_groups, weight_paint):
        self.name = name
        self.verts = vertices
        self.edges = edges
        self.faces = faces
        self.vtx_groups = vtx_groups
        self.weight_paint = weight_paint

    def to_tuple(self):
        return self.name, self.verts, self.edges, self.faces, self.vtx_groups, self.weight_paint

    @classmethod
    def fromTuple(cls, data):
        return cls(data[0], data[1], data[2], data[3], data[4], data[5])

    @classmethod
    def fromBlenderObject(cls, object):
        mesh = bmesh.from_edit_mesh(object.data)
        return cls(
            object.name,
            [v.co.to_tuple() for v in mesh.verts],
            [[v.index for v in e.verts] for e in mesh.edges],
            [[v.index for v in f.verts] for f in mesh.faces],
            [group.name for group in object.vertex_groups],
            [[(vg.group, vg.weight) for vg in vtx.groups] for vtx in object.data.vertices]
        )


def extract_mesh():
    with mode.active_mode_ctx(mode.MODE_EDIT):
        return Mesh.fromBlenderObject(context.get_object())

        # object_name = obj.name
        # mesh = bmesh.from_edit_mesh(obj.data)

        # vertices = [v.co.to_tuple() for v in mesh.verts]
        # edges = [[v.index for v in e.verts] for e in mesh.edges]
        # faces = [[v.index for v in f.verts] for f in mesh.faces]

        # vtx_groups = [g.name for g in obj.vertex_groups]
        # weight_paint = [[(vg.group, vg.weight) for vg in v.groups] for v in obj.data.vertices]

        # return object_name, vertices, edges, faces, vtx_groups, weight_paint
