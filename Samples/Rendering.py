import bpy

def renderToPng(pngFilepath):
    bpy.context.scene.render.filepath = pngFilepath
    bpy.ops.render.render(write_still = True)
