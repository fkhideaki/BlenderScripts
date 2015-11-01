bl_info = {
    "name": "ToolShelf template",
    "author": "fkhd",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Tool Shelf > ToolShelfSampleTab",
    "description": "Exporter plugin template",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}


import bpy


class ToolshelTestCmd1(bpy.types.Operator):
    bl_idname = "view3d.toolshelftest_testcmd1"
    bl_label = "TestCmd"
    def execute(self, context):
        print("test1")
        return {'FINISHED'}
    
class ToolshelTestCmd2(bpy.types.Operator):
    bl_idname = "view3d.toolshelftest_testcmd2"
    bl_label = "TestCmd"
    msg = ""
    def execute(self, context):
        print("test2")
        return {'FINISHED'}

# main class of this toolbar
class VIEW3D_PT_3dnavigationPanel(bpy.types.Panel):
    bl_category = "SampleTab"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_label = "SamplePanel"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        col = layout.column(align=True)
        col.label(text="commands:")
        row = col.row()
        row.operator("view3d.toolshelftest_testcmd1", text="test1")
        row.operator("view3d.toolshelftest_testcmd2", text="test2")

def register():
    bpy.utils.register_class(ToolshelTestCmd1)
    bpy.utils.register_class(ToolshelTestCmd2)
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_class(ToolshelTestCmd1)
    bpy.utils.unregister_class(ToolshelTestCmd2)
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
