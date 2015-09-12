import bpy
import cmath

def calcArea3D(mesh):
    area = 0.0
    for f in mesh.polygons:
        area += f.area
    return area

def calcTriArea2d(uv0, uv1, uv2):
    d10 = uv1 - uv0
    d20 = uv2 - uv0
    return d10.x * d20.y - d10.y * d20.x

def calcArea2D(mesh):
    area = 0.0
    uv_layer = mesh.uv_layers.active
    uvs = uv_layer.data.values()

    uvo = 0
    for f in mesh.polygons:
        lvid = 0
        numTris = len(f.vertices) - 2
        for tid in range(0, numTris):
            uv0 = uvs[lvid + uvo + 0].uv
            uv1 = uvs[lvid + uvo + tid + 1].uv
            uv2 = uvs[lvid + uvo + tid + 2].uv
            a = calcTriArea2d(uv0, uv1, uv2)
            area += abs(a)
        uvo += len(f.vertices)
    return area

def texcoordTo3D(mesh):
    area2d = calcArea2D(mesh)
    area3d = calcArea3D(mesh)
    scale = cmath.sqrt(area3d / area2d).real
    
    uv_layer = mesh.uv_layers.active
    uvs = uv_layer.data.values()

    uvo = 0
    for f in mesh.polygons:
        lvid = 0
        for vid in f.vertices:
            v = mesh.vertices[vid]
            uv = uvs[lvid + uvo]
            lvid += 1
            v.co.x = uv.uv.x * scale
            v.co.y = uv.uv.y * scale
            v.co.z = 0
        uvo += len(f.vertices)

def texcoordTo3DAllSels():
    for obj in bpy.data.objects:
        if not obj.select:
            continue
        if obj.type != 'MESH':
            continue
        m = obj.data
        texcoordTo3D(m)

texcoordTo3DAllSels()
