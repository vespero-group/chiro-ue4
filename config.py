import bpy


class Config(bpy.types.AddonPreferences):
    bl_idname = __package__

    _properties = 'advanced_mode', 'developer_mode'

    p_advanced_mode: bpy.props.BoolProperty(
        name="Advanced features",
        description="Show the advanced elements in the UI (tools for uncommon use cases)",
        default=False
    )
    p_developer_mode: bpy.props.BoolProperty(
        name="Developer mode",
        description="Show the UIs intended for developers of this addon",
        default=False
    )

    def draw(self, ctx):
        for key in self._properties:
            self.layout.prop(self, 'p_{}'.format(key))

    def get(self, key, default=None):
        if key in self._properties:
            return getattr(self, 'p_{}'.format(key), default)
