def get_config():
    from . import context
    from .. import config

    return context.get().preferences.addons[config.Config.bl_idname].preferences


def get(key, default=None):
    return get_config().get(key, default)


def is_advanced_mode():
    return get('advanced_mode', False) or is_developer_mode()


def is_developer_mode():
    return get('developer_mode', False)
