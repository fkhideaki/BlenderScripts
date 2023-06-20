import bpy


def OpenObj(filename):
    bpy.ops.import_scene.obj(filepath=filename)
