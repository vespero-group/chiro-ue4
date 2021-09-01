from math import radians
from mathutils import Matrix
from . import arma
from .bone import Bone


class Transform:
    __slots__ = ()


class SingleBoneTransform(Transform):
    __slots__ = 'target_bone_name',

    def __init__(self, bone_name):
        self.target_bone_name = bone_name

    def checkBoneNeedsTransform(self, bone):
        return bone.name == self.target_bone_name


class CallBack(Transform):
    __slots__ = 'the_callback'

    def __init__(self, the_callback):
        self.the_callback = the_callback

    def transform(self, armature):
        result = self.the_callback(armature)
        return result if isinstance(result, Bone) else armature


class CallBackRecursively(CallBack):
    def transform(self, armature):
        def _recursively(bone, action):
            result = action(bone)
            bone = result if isinstance(result, Bone) else bone

            return bone.callback(
                lambda a: a,
                lambda c: [_recursively(b, action) for b in c]
            )

        return _recursively(armature, self.the_callback)


class SingleBoneCallback(CallBackRecursively):
    __slots__ = SingleBoneTransform.__slots__

    def __init__(self, bone_name, the_callback=None):
        if the_callback is None:
            the_callback = self._transform
        super(CallBackRecursively, self).__init__(the_callback)
        SingleBoneTransform.__init__(self, bone_name)

    def transform(self, armature):
        def _recursively(bone, action):
            if SingleBoneTransform.checkBoneNeedsTransform(self, bone):
                result = action(bone)
                bone = result if isinstance(result, Bone) else bone

            return bone.callback(
                lambda a: a,
                lambda c: [_recursively(b, action) for b in c]
            )

        return _recursively(armature, self.the_callback)


class Rename(CallBackRecursively):
    __slots__ = 'rename_map',

    def __init__(self, rename_map):
        super().__init__(self._transform)
        self.rename_map = rename_map

    def _transform(self, bone):
        if bone.name in self.rename_map:
            arma.get_bone(bone.name).name = self.rename_map[bone.name]
            return bone.callback(
                lambda n: self.rename_map[n] if n in self.rename_map else n,
                lambda c: c
            )


class ReRoll(SingleBoneCallback):
    __slots__ = 'roll',

    def __init__(self, bone_name, bone_roll):
        super().__init__(bone_name, self._transform)
        self.roll = bone_roll

    def _transform(self, bone):
        arma.get_bone(bone.name).roll = self._get_roll(bone)

    def _get_roll(self, bone):
        if isinstance(self.roll, Matrix):
            return self._get_rotation_delta(bone, self.roll)
        else:
            return radians(self.roll)

    def _get_rotation_delta(self, bone, roll):
        edit_bone = arma.get_bone(bone.name)
        current = edit_bone.matrix
        expected = roll
        delta = current.inverted() @ expected

        _, delta_roll, _ = delta.decompose()

        return edit_bone.roll + delta_roll.to_euler().y


class Delete(SingleBoneCallback):
    def _transform(self, bone):
        arma.delete_bone(bone.name)


class SnapToChild(SingleBoneCallback):
    __slots__ = 'child_name',

    def __init__(self, bone_name, child_name=None):
        super().__init__(bone_name, self._transform)
        self.child_name = child_name

    def _transform(self, bone):
        if len(bone.children) != 1 and not self.child_name:
            raise Exception('Bone {} has many children'.format(bone.name))

        ebone = arma.get_bone(bone.name)
        child = arma.get_bone(self.child_name if self.child_name else bone.children[0].name)

        ebone.tail = child.head.copy()
        child.use_connect = True
