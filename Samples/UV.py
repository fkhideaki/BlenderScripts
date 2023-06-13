import bpy

def applyVertSelToUV(mesh):
    if not bpy.data.scenes[0].tool_settings.use_uv_select_sync:
        return

    uvl = mesh.uv_layers.active
    uvs = uvl.data.values()

    uvIdx = 0
    for f in mesh.polygons:
        for vid in f.vertices:
            v = mesh.vertices[vid]
            uv = uvs[uvIdx]
            uv.select = v.select
            uvIdx += 1
