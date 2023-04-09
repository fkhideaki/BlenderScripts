import bpy

def removeAllVerts():
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.delete(type='VERT')
