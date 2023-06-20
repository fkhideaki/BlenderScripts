import bpy

def assignEachShapeyeToFrames(obj):
    ms = obj.data

    numKeys = len(obj.data.shape_keys.key_blocks)
    ms.shape_keys.use_relative = False
    for i in range(numKeys):
        obj.active_shape_key_index = i
        sk = bpy.data.shape_keys[0]
        sk.eval_time = i * 10
        sk.keyframe_insert(data_path='eval_time', frame=i)

def mergeMeshToEachShapeKeys():
    sels = []
    act = None
    for o in bpy.data.objects:
        if o.type != 'MESH':
            o.select_set(False)
            continue
        if o.select_get() and o.visible_get():
            oo = o.copy()
            oo.data = o.data.copy()
            bpy.context.scene.collection.objects.link(oo)
            if o is bpy.context.active_object:
                bpy.context.view_layer.objects.active = oo
                act = oo
            o.select_set(False)
            oo.select_set(True)
            sels.append(oo)

    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.join_shapes()
    act.data.shape_keys.use_relative = False

    act.select_set(False)
    for o in sels:
        if not o is act:
            bpy.context.view_layer.objects.active = o
            break
    bpy.ops.object.delete(use_global=False)

    bpy.context.view_layer.objects.active = act
    act.select_set(True)
