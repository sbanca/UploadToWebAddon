import bpy
import tempfile
import os
import time
import requests
from datetime import datetime

class Upload(bpy.types.Operator):
    bl_idname = "view3d.export_to_web"
    bl_label = "Covert to gltf and upload to web"
    bl_description = "Export to Web"

    def execute(self, context):

        if "gltf" not in dir(bpy.ops.export_scene):
            print("Make sure to have glTF exporter installed first")
            print("https://github.com/KhronosGroup/glTF-Blender-Exporter")
            quit()

        path = tempfile.gettempdir()
        t = str(int(datetime.timestamp(datetime.now())))
        gltf ='model-'+t+'.glb'
        bin = 'model-'+t+'.bin'

        filepath = os.path.join(path, gltf)

        print(filepath)

        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.export_scene.gltf(filepath=filepath)

        AFrameContentTemplate = '''<html>
        <head>
            <script src="https://aframe.io/releases/0.6.1/aframe.min.js"></script>
            <script src="//cdn.rawgit.com/donmccurdy/aframe-extras/v3.10.0/dist/aframe-extras.min.js"></script>
        </head>
        <body>
            <a-scene>
            <a-sky color="lightblue"></a-sky>
            <a-entity gltf-model-next="GLTF" animation-mixer position="0 1 -2"></a-entity>
            </a-scene>
        </body>
        </html>
        '''

        if not len(bpy.data.actions):
            AFrameContentTemplate.replace("animation-mixer", "")

        with open(filepath, 'rb') as f:
            r = requests.post(bpy.context.scene.URLProps, files={'userfile': f})

        filepath = os.path.join(path, bin)
        with open(filepath, 'rb') as f:
            r = requests.post(bpy.context.scene.URLProps, files={'userfile': f})

        print('done')

        AFrameContent = AFrameContentTemplate.replace("GLTF", gltf)
        aframe = tempfile.NamedTemporaryFile(delete=False)
        with open(aframe.name, 'w') as f:
            f.write(AFrameContent)
            # file is not immediately deleted, cf delete=False

        import json
        with open(aframe.name, 'rb') as f:
            r = requests.post(bpy.context.scene.URLProps, files={'userfile': f})
            res = json.loads(str(r.text))

        #os.unlink(aframe.name)
        if (res["result"]):
            aframeExperienceUrl = bpy.context.scene.URLProps +"uploads/"+res["result"]
            print("visit "+aframeExperienceUrl)

            import webbrowser
            webbrowser.open(aframeExperienceUrl)

        return {'FINISHED'}