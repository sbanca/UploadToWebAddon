# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Create Addon Tutorial
# https://www.youtube.com/watch?v=uahfuypQQ04
# https://github.com/JacquesLucke/blender_vscode
#

bl_info = {
    "name" : "Export to WebVR",
    "author" : "Riccardo",
    "description" : "Simple test addon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy 

from . upload import Upload
from . panel import UIPanel
from . props import GlobalProps
from . upload_firestore import UploadFirestore

classes =(Upload,UIPanel,GlobalProps,UploadFirestore)

def register():

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
    bpy.types.Scene.GlobalProps = bpy.props.PointerProperty(type=GlobalProps)


def unregister():

    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    del(bpy.types.Scene.GlobalProps)