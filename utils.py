import bpy
import tempfile
import os
import time
import requests
import json
from datetime import datetime
import platform


def save_file_glb():
    
    #############
    # Save File #   
    #############

    path = tempfile.gettempdir()
    t = str(int(datetime.timestamp(datetime.now())))
    glb ='model-'+t+'.glb'

    file_path_glb = os.path.join(path, glb)

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.export_scene.gltf(export_format='GLB',filepath=file_path_glb)      

    return path,glb,file_path_glb

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