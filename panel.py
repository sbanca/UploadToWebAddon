import bpy 
from . url import URLProps

class UIPanel(bpy.types.Panel):
    bl_idname = "UIPanel"
    bl_label = "Export to WebVR"
    bl_category = "Export to WebVR Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        props = bpy.context.scene.URLProps
        layout = self.layout       
        layout.row().prop(props, "url", text="url")
        layout.row().operator('view3d.export_to_web_vr', text="Export to WebVR")