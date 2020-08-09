from . import MESHES
from ..utils.mesh import Mesh


def get(model_id, variant_id):
    vkey = variant_key(model_id, variant_id)

    if vkey is None:
        raise Exception('Unknown mesh model-variant "{}:{}"'.format(model_id, variant_id))

    m, v = vkey
    data = MESHES[m]['variants'][v]['load_data']()

    return Mesh.fromTuple(data)


def variant_key(model_id, variant_id):
    model_key = None
    variant_key = None

    for key in range(0, len(MESHES)):
        if MESHES[key]['id'] == model_id:
            model_key = key
            break

    if model_key is None:
        return None

    variants = MESHES[model_key]['variants']
    for key in range(0, len(variants)):
        if variants[key]['id'] == variant_id:
            variant_key = key
            break

    if variant_key is None:
        return None

    return model_key, variant_key


def get_by_option_key(option_key):
    m, v = list(map(int, option_key.split(':')))
    data = MESHES[m]['variants'][v]['load_data']()
    return Mesh.fromTuple(data)


def gen_option_key(model_id, variant_id):
    return '{}:{}'.format(*variant_key(model_id, variant_id))


def get_options_generator(filter=None):
    def _options(self, ctx=None):
        result = []
        for model_key in range(0, len(MESHES)):
            model = MESHES[model_key]

            for variant_key in range(0, len(model['variants'])):
                variant = model['variants'][variant_key]

                if filter and not filter(model['id'], variant['id']):
                    continue

                option_key = '{}:{}'.format(model_key, variant_key)
                option_name = '{} --> {}'.format(
                    model['name'], variant['name'])

                result.append((option_key, option_name, ""))

        return result

    return _options
