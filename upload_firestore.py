import bpy
import tempfile
import os
import time
import requests
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
from . utils import save_file_glb, getDirectory
from . props import GlobalProps
import json


class UploadFirestore(bpy.types.Operator):
    bl_idname = "view3d.upload_to_firestore"
    bl_label = "Covert to gltf,bin and upload to firestore"
    bl_description = "Upload to Firestore"

    def execute(self, context):

        
        #############
        # Save File #   
        #############

        path,glb,file_path_glb = save_file_glb()

        ######################
        # upload to firebase #
        ######################

        certificateFilePath = bpy.context.scene.GlobalProps.firebase_certificate

        cred = credentials.Certificate(certificateFilePath)

        if bpy.context.scene.GlobalProps.app_name in firebase_admin._apps: 
            app =  firebase_admin._apps[bpy.context.scene.GlobalProps.app_name]
        else:
            app = firebase_admin.initialize_app(cred, {'storageBucket':bpy.context.scene.GlobalProps.firebase_url}, bpy.context.scene.GlobalProps.app_name )

        db = firestore.client(app=app)
        bucket = storage.bucket(app=app)
        
        ##upload the files       
        print("upload to --> gs://" + bucket.name)  # "[DEFAULT]"

        blob = bucket.blob(glb)
        with open(file_path_glb, 'rb') as f:
            blob.upload_from_file(f)
            print(blob.public_url)
        
        
        return {'FINISHED'}

