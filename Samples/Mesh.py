import bpy
import bmesh

def removeAllVerts():
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.reveal()
    bpy.ops.mesh.delete(type='VERT')

def getCurrentBMesh():
    o = bpy.context.active_object
    m = o.data
    bm = bmesh.from_edit_mesh(m)
    return bm

def bmeshDeselectSample():
    o = bpy.context.active_object
    m = o.data
    bm = getBM()
    bm.verts[0].select = False
    bm.select_flush_mode()
    m.update()
