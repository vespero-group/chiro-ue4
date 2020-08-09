from . import TRANSFORMS
from ..utils.mesh import Mesh


def get(model_id, variant_id):
    vkey = variant_key(model_id, variant_id)

    if vkey is None:
        raise Exception('Unknown transform model-variant "{}:{}"'.format(model_id, variant_id))

    m, v = vkey
    return (TRANSFORMS[m], TRANSFORMS[m]['variants'][v])


def variant_key(model_id, variant_id):
    model_key = None
    variant_key = None

    for key in range(0, len(TRANSFORMS)):
        if TRANSFORMS[key]['id'] == model_id:
            model_key = key
            break

    if model_key is None:
        return None

    variants = TRANSFORMS[model_key]['variants']
    for key in range(0, len(variants)):
        if variants[key]['id'] == variant_id:
            variant_key = key
            break

    if variant_key is None:
        return None

    return model_key, variant_key


def get_by_option_key(option_key):
    m, v = list(map(int, option_key.split(':')))
    return (TRANSFORMS[m], TRANSFORMS[m]['variants'][v])


def gen_option_key(model_id, variant_id):
    return '{}:{}'.format(*variant_key(model_id, variant_id))


def get_options_generator(filter=None, ctx_for_poll=None):
    def _options(self, ctx=None):
        result = []
        for model_key in range(0, len(TRANSFORMS)):
            model = TRANSFORMS[model_key]

            if ctx_for_poll and 'poll' in model and not model['poll'](ctx_for_poll):
                continue

            for variant_key in range(0, len(model['variants'])):
                variant = model['variants'][variant_key]

                if ctx_for_poll and 'poll' in variant and not variant['poll'](ctx_for_poll):
                    continue

                if filter and not filter(model['id'], variant['id']):
                    continue

                option_key = '{}:{}'.format(model_key, variant_key)
                option_name = '{} --> {}'.format(model['name'], variant['name'])
                option_desc = variant['description']

                result.append((option_key, option_name, option_desc))

        return result

    return _options
