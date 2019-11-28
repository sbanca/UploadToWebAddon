import bpy

class URLProps(bpy.types.PropertyGroup):

    url: bpy.props.StringProperty(default="http://yourserver.xyz/backend/")