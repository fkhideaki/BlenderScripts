bl_info = {
    "name": "Exporter template",
    "author": "fkhd",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "File > Export > exporter template (.txt)",
    "description": "Exporter plugin template",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export",
}


import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty
from bpy.types import Operator


def writeMain(context, filepath):
    f = open(filepath, 'w', encoding='utf-8')
    f.write("Hello\n")
    f.close()
    return {'FINISHED'}

class ExporterTemplate(Operator, ExportHelper):
    bl_idname = "exporter_template.export_file"
    bl_label = "Export data"
    bl_description = 'Plugin description text'

    filename_ext = ".txt"

    filter_glob = StringProperty(
            default = "*" + ".txt",
            options = {'HIDDEN'},
            )

    def execute(self, context):
        return writeMain(context, self.filepath)


def menu_func_export(self, context):
    self.layout.operator(ExporterTemplate.bl_idname, text = "Exporter template")

def register():
    bpy.utils.register_class(ExporterTemplate)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExporterTemplate)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()
