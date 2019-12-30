import bpy 
from . props import GlobalProps
from . utils import getDirectory

class UIPanel(bpy.types.Panel):
    bl_idname = "UIPanel"
    bl_label = "Export to WebVR"
    bl_category = "Export to WebVR Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    directory = "Save your Firebase Certificate here --> " + getDirectory()

    def draw(self, context):
        props = bpy.context.scene.GlobalProps
        layout = self.layout       
        
        #global values management 
        layout.row().operator('view3d.save_values', text="Save values")
        layout.row().operator('view3d.load_values', text="Load Values")

        #upload webvr 
        layout.row().prop(props, "uploadUrl", text="uploadUrl")
        layout.row().prop(props, "viewUrl", text="viewUrl")
        layout.row().operator('view3d.export_to_web_vr', text="Export to WebVR")
        layout.label(text="") 

        #upload firebase
        layout.row().prop(props, "firebase_url", text="Firebase Url")
        layout.row().label(text=self.directory)
        layout.row().prop(props, "firebase_certificate", text="Firebase Certificate")
        layout.row().operator('view3d.upload_to_firestore', text="Upload to Firestore")
