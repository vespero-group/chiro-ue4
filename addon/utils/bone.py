from mathutils import Matrix, Vector


class Bone:
    '''Bone Node for Armature description'''
    __slots__ = 'name', 'children'

    def __init__(self, name, children=None):
        self.name = name
        self.children = children if children else []

    def format(self, *args, **kwargs):
        return Bone(
            self.name.format(*args, **kwargs),
            [bone.format(*args, **kwargs) for bone in self.children]
        )

    def get_bone(self, name):
        if self.name == name:
            return self

        for child in self.children:
            bone = child.get_bone(name)
            if bone:
                return bone

        return None

    def recursively(self, action, parent=None):
        result = action(self, parent)
        bone = result if isinstance(result, Bone) else self

        return bone.callback(
            lambda a: a,
            lambda c: [b.recursively(action, parent=bone) for b in c]
        )

    def callback(self, name_callback, children_callback):
        return Bone(
            name_callback(self.name),
            children_callback(self.children)
        )

    def get_bone_names_recursively(self):
        result = {self.name}

        for child in self.children:
            result.update(child.get_bone_names_recursively())

        return result

    def to_tuple(self):
        return self.name, [c.to_tuple() for c in self.children]

    @classmethod
    def fromTuple(cls, data):
        return cls(data[0], [cls.fromTuple(c) for c in data[1]])


class EditBone(Bone):
    '''EditBone Node for Armature description (with bone data)

       Data:
         - roll : int = EditBone.roll
         - head : Vector = EditBone.head
         - tail : Vector = EditBone.tail
         - mtx : Matrix = EditBone.matrix
         - connect : bool = EditBone.use_connect
         - parent_name : str = EditBone.parent.name
    '''
    __slots__ = 'roll', 'head', 'tail', 'mtx', 'connect', 'parent_name'

    def __init__(self, name, roll, head, tail, mtx, connect, children=None, parent_name=None):
        super().__init__(name, children)
        self.roll = roll
        self.head = head
        self.tail = tail
        self.mtx = mtx
        self.connect = connect
        self.parent_name = parent_name

    def editbone_restore(self, edit_bone):
        '''Restore the settings of the Blender EditBone'''
        edit_bone.name = self.name
        edit_bone.roll = self.roll
        edit_bone.head = self.head
        edit_bone.tail = self.tail
        edit_bone.matrix = self.mtx
        edit_bone.use_connect = self.connect

    def to_tuple(self):
        return (
            self.name,
            [c.to_tuple() for c in self.children],
            self.roll,
            self.head.to_tuple(),
            self.tail.to_tuple(),
            [row.to_tuple() for row in self.mtx.row],
            int(self.connect),
            self.parent_name
        )

    @classmethod
    def fromTuple(cls, data):
        return cls(
            data[0],
            data[2],
            Vector(data[3]),
            Vector(data[4]),
            Matrix(data[5]),
            bool(data[6]),
            [cls.fromTuple(c) for c in data[1]],
            data[7]
        )

    @classmethod
    def fromBlenderEditBone(cls, bone):
        return cls(
            bone.name,
            bone.roll,
            bone.head.copy(),
            bone.tail.copy(),
            bone.matrix.copy(),
            bone.use_connect,
            [cls.fromBlenderEditBone(c) for c in bone.children],
            bone.parent.name if bone.parent else None
        )
