from . import ARMATURES
from ..utils.bone import Bone, EditBone


def get(model_id, variant_id):
    vkey = variant_key(model_id, variant_id)

    if vkey is None:
        raise Exception(
            'Unknown model armature variant "{}:{}"'.format(model_id, variant_id))

    m, v = vkey
    data = ARMATURES[m]['variants'][v]['load_data']()

    return Bone('root', [EditBone.fromTuple(t) for t in data])


def variant_key(model_id, variant_id):
    model_key = None
    variant_key = None

    for key in range(0, len(ARMATURES)):
        if ARMATURES[key]['id'] == model_id:
            model_key = key
            break

    if model_key is None:
        return None

    variants = ARMATURES[model_key]['variants']
    for key in range(0, len(variants)):
        if variants[key]['id'] == variant_id:
            variant_key = key
            break

    if variant_key is None:
        return None

    return model_key, variant_key


def get_by_option_key(option_key):
    m, v = list(map(int, option_key.split(':')))
    data = ARMATURES[m]['variants'][v]['load_data']()
    return Bone('root', [EditBone.fromTuple(t) for t in data])


def gen_option_key(model_id, variant_id):
    return '{}:{}'.format(*variant_key(model_id, variant_id))


def get_options_generator(filter=None):
    def _options(self, ctx=None):
        result = []
        for armature_key in range(0, len(ARMATURES)):
            armature = ARMATURES[armature_key]

            for variant_key in range(0, len(armature['variants'])):
                variant = armature['variants'][variant_key]

                if filter and not filter(armature['id'], variant['id']):
                    continue

                option_key = '{}:{}'.format(armature_key, variant_key)
                option_name = '{} --> {}'.format(armature['name'], variant['name'])

                result.append((option_key, option_name, ""))

        return result

    return _options
