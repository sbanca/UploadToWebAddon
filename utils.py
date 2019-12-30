import bpy
import tempfile
import os
import time
import requests
import json
from datetime import datetime
import platform


def save_file_gltf_bin():
    
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

    return path,gltf,bin,file_path_gltf,file_path_bin

def getDirectory():

        if platform.system() == "Windows":       
            directory = os.environ['USERPROFILE']+"\\AppData\\Roaming\\Blender Foundation\\Blender\\2.81"
        elif platform.system() == "Linux":  
            directory = os.environ['HOME']+"\\.config\\blender\\2.81"
        elif platform.system() == "MACOSX":  
            directory = "user\\"+os.environ['USER']+"\\Library\\Application Support\\Blender\\2.81"
        else:
            directory=None

        return directory 