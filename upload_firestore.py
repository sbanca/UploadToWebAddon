import bpy
import tempfile
import os
import time
import requests
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth

class UploadFirestore(bpy.types.Operator):
    bl_idname = "view3d.upload_to_firestore"
    bl_label = "Covert to gltf,bin and upload to firestore"
    bl_description = "Upload to Firestore"

    def execute(self, context):
        
        #############
        # Save File #   
        #############

        path = tempfile.gettempdir()
        t = str(int(datetime.timestamp(datetime.now())))
        gltf ='model-'+t+'.gltf'
        bin = 'model-'+t+'.bin'

        file_path_gltf = os.path.join(path, gltf)
        file_path_bin = os.path.join(path, bin)

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.export_scene.gltf(export_format='GLTF_SEPARATE',filepath=file_path_gltf)      

        ######################
        # upload to firebase #
        ######################

        cred = credentials.Certificate("privateKey/gltf-storage-firebase-adminsdk-b3kbp-8952bc56e8.json")
        app = firebase_admin.initialize_app(cred, {'storageBucket': 'gltf-storage.appspot.com'})
        db = firestore.client()
        bucket = storage.bucket()

        # Initialize the default app
        print("ready to upload --> gs://" + bucket.name)  # "[DEFAULT]"

        blob = bucket.blob(gltf)
        with open(file_path_gltf, 'rb') as f:
            blob.upload_from_file(f)

        blob = bucket.blob(bin)
        with open(file_path_bin, 'rb') as f:
            blob.upload_from_file(f)
            

        
        return {'FINISHED'}