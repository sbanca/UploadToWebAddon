import bpy

class GlobalProps(bpy.types.PropertyGroup):

    url: bpy.props.StringProperty(default="http://localhost:3000")
    firebase_url: bpy.props.StringProperty(default="gltf-storage.appspot.com")
    firebase_certificate: bpy.props.StringProperty(default="privateKey/gltf-storage-firebase-adminsdk-b3kbp-8952bc56e8.json")
    temp_file_name: bpy.props.StringProperty()