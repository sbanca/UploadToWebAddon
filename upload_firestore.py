import bpy
import tempfile
import os
import time
import requests
import json
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
from . utils import save_file_gltf_bin, getDirectory
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

        path,gltf,bin,file_path_gltf,file_path_bin = save_file_gltf_bin()

        ######################
        # upload to firebase #
        ######################

        certificateFilePath = getDirectory() + '\\' + bpy.context.scene.GlobalProps.firebase_certificate

        cred = credentials.Certificate(certificateFilePath)

        if bpy.context.scene.GlobalProps.app_name in firebase_admin._apps: 
            app =  firebase_admin._apps[bpy.context.scene.GlobalProps.app_name]
        else:
            app = firebase_admin.initialize_app(cred, {'storageBucket':bpy.context.scene.GlobalProps.firebase_url}, bpy.context.scene.GlobalProps.app_name )

        db = firestore.client(app=app)
        bucket = storage.bucket(app=app)
        
        ##get the list 
        blob = bucket.blob("list.json")
        directory = os.path.join(tempfile.gettempdir(),"temp.json")
        
        try: 
            blob.download_to_filename(directory)

            with open(directory) as json_file:  
                data = json.load(json_file)
        
        except: 
            data={'list':[]} 

        ##upload the files       
        print("upload to --> gs://" + bucket.name)  # "[DEFAULT]"

        blob = bucket.blob(gltf)
        with open(file_path_gltf, 'rb') as f:
            blob.upload_from_file(f)
            print(blob.public_url)

        blob = bucket.blob(bin)
        with open(file_path_bin, 'rb') as f:
            blob.upload_from_file(f)
            print(blob.public_url)

        data['list'].append(gltf)
        data['list'].append(bin)
        blob = bucket.blob("list.json")

        ##upload the list 
        with open(directory, 'w') as outfile:
            json.dump(data, outfile)
            
        with open(directory, 'rb') as f:
            blob.upload_from_file(f)
            
        
        return {'FINISHED'}

