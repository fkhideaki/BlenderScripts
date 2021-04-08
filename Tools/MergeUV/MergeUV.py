import bpy


def toMeshMode():
    bpy.ops.object.mode_set(mode = 'EDIT_MESH')

def toObjectMode():
    bpy.ops.object.mode_set(mode = 'OBJECT')

def getSecondarySel():
    act = bpy.context.active_object
    for obj in bpy.data.objects:
        if not obj.type == 'MESH':
            continue
        if not obj == act:
            return obj
    raise Exception('Secondary mesh is not exist')


def mergeUVselToActive():
    toObjectMode()

    obj0 = bpy.context.active_object
    obj1 = getSecondarySel()
    if obj0 == None:
        raise Exception('Active is not selected')

    uvs1 = obj1.data.uv_layers
    print(len(uvs1))
    if not len(uvs1) == 1:
        raise Exception('Secondary must have single uv layer')
    uv1 = obj1.data.uv_layers[0].data

    if not obj0.type == 'MESH':
        raise Exception('Active is not mesh')
    bpy.ops.mesh.uv_texture_add()
    uvs0 = obj0.data.uv_layers
    uv0 = uvs0.active.data

    if not len(uv0) == len(uv1):
        raise Exception('Num uv is not match')

    num = len(uv0)
    for i in range(0, num):
       uv0[i].uv = uv1[i].uv
