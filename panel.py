import bpy 
from . props import GlobalProps

class UIPanel(bpy.types.Panel):
    bl_idname = "UIPanel"
    bl_label = "Export to WebVR"
    bl_category = "Export to WebVR Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        props = bpy.context.scene.GlobalProps
        layout = self.layout       
        
        #upload webvr 
        layout.row().prop(props, "url", text="url")
        layout.row().operator('view3d.export_to_web_vr', text="Export to WebVR")

        #upload firebase
        layout.row().prop(props, "firebase_url", text="Firebase Url")
        layout.row().prop(props, "firebase_certificate", text="Firebase Certificate")
        layout.row().operator('view3d.upload_to_firestore', text="Upload to Firestore")
