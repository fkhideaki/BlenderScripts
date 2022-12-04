import bpy
import bmesh

def addSegment(v0, v1):
    bpy.ops.object.editmode_toggle()

    o = bpy.context.active_object
    ms = o.data
    bm = bmesh.new()
    bm.from_mesh(ms)

    v0 = bm.verts.new(v0)
    v1 = bm.verts.new(v1)

    bm.edges.new((v0, v1))

    bm.to_mesh(ms)
    bm.free()

    bpy.ops.object.editmode_toggle()
    
addSegment((0, 0, 0), (1, 1, 1))
