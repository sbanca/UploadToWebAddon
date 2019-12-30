import bpy
import json
import os.path
from os import path
import platform
from . utils import getDirectory

class GlobalProps(bpy.types.PropertyGroup):

    uploadUrl: bpy.props.StringProperty(default="http://localhost:3000/upload")
    viewUrl: bpy.props.StringProperty(default="http://localhost:3000/download/")
    firebase_url: bpy.props.StringProperty(default="gltf-storage.appspot.com")
    firebase_certificate: bpy.props.StringProperty(default="gltf-storage-firebase-adminsdk-b3kbp-8952bc56e8.json")
    temp_file_name: bpy.props.StringProperty()
    app_name: bpy.props.StringProperty(default="blender gltf upload")

class GlobalPropsLoad(bpy.types.Operator):
    bl_idname = "view3d.load_values"
    bl_label = "Load Values"
    bl_description = "Load Values"


    def execute(self, context):
        props = bpy.context.scene.GlobalProps
        
        directory = getDirectory() + "\\global.json"

        if directory == None: return 

        if path.exists(directory):#open file
            
            print('global.json found')

            with open(directory) as json_file:
                
                data = json.load(json_file)
                bpy.context.scene.GlobalProps.uploadUrl = data['uploadUrl']
                bpy.context.scene.GlobalProps.viewUrl = data['viewUrl'] 
                bpy.context.scene.GlobalProps.firebase_url = data['firebase_url']
                bpy.context.scene.GlobalProps.firebase_certificate = data['firebase_certificate']
                bpy.context.scene.GlobalProps.temp_file_name = data['temp_file_name']
                bpy.context.scene.GlobalProps.app_name = data['app_name']
        
        else:#create file
            
            with open(directory, 'w') as outfile:

                data = {
                'uploadUrl':bpy.context.scene.GlobalProps.uploadUrl,
                'viewUrl':bpy.context.scene.GlobalProps.viewUrl,
                'firebase_url':bpy.context.scene.GlobalProps.firebase_url,
                'firebase_certificate':bpy.context.scene.GlobalProps.firebase_certificate,
                'temp_file_name':bpy.context.scene.GlobalProps.temp_file_name,
                'app_name':bpy.context.scene.GlobalProps.app_name}
        
                json.dump(data, outfile)

                print('gloabal.json created')
                
        return {'FINISHED'}

class GlobalPropsSave(bpy.types.Operator):
    bl_idname = "view3d.save_values"
    bl_label = "Save Values"
    bl_description = "Save Values"

    def execute(self, context):
        props = bpy.context.scene.GlobalProps

        directory = getDirectory() + "\\global.json"

        if directory == None: return 
        
        with open(directory, 'w') as outfile:

            data = {
            'uploadUrl':bpy.context.scene.GlobalProps.uploadUrl,
            'viewUrl':bpy.context.scene.GlobalProps.viewUrl,
            'firebase_url':bpy.context.scene.GlobalProps.firebase_url,
            'firebase_certificate':bpy.context.scene.GlobalProps.firebase_certificate,
            'temp_file_name':bpy.context.scene.GlobalProps.temp_file_name,
            'app_name':bpy.context.scene.GlobalProps.app_name}
    
            json.dump(data, outfile)

            print('global.json created')

        return {'FINISHED'}