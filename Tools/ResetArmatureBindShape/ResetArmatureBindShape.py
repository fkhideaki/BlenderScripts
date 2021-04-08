import bpy

def getInvert(m):
    mi = m.copy()
    mi.invert()
    return mi

def toEditMode():
    bpy.ops.object.mode_set(mode = 'EDIT')
def toPoseMode():
    bpy.ops.object.mode_set(mode = 'POSE')
def toObjectMode():
    bpy.ops.object.mode_set(mode = 'OBJECT')

def clearConstraints(bx):
    if len(bx.constraints) == 0:
        return
    cc = [c for c in bx.constraints if True]
    for c in cc:
        bx.constraints.remove(c)

def assignCopyTrans(bx, dst, bone):
    bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
    con = bx.constraints["Copy Transforms"]
    con.target = dst
    con.subtarget = bone.name

def makeConstraint(ar, bone, dst):
    toPoseMode()
    bpy.ops.pose.select_all(action='DESELECT')
    toObjectMode()
    bone.select = True
    ar.bones.active = bone
    toPoseMode()
    bn = bone.name
    bx = bpy.context.object.pose.bones[bn]
    clearConstraints(bx)
    assignCopyTrans(bx, dst, bone)

def getFirstNonActiveSelObject():
    for o in bpy.context.selected_objects:
        if not o.name == bpy.context.active_object.name:
            return o
    
def syncBoneTrans(tar, dst):
    tarBone = tar.data
    dstBone = dst.data
    beforeMode = bpy.context.active_object.mode
    toObjectMode()
    for tb in tarBone.bones:
        makeConstraint(tarBone, tb, dst)
    bpy.ops.object.mode_set(mode = beforeMode)

def verifyIsValidArmature(a):
    if not a.type == 'ARMATURE':
        raise Exception("object ['{}'] is not armature".format(a.name))

def verifyArmatureTopology(a, b):
    ab = a.data.bones
    bb = b.data.bones
    if not len(ab) == len(bb):
        raise Exception('Num bones is not same')
    n = len(ab)
    for i in range(0, n):
        an = ab[i].name
        bn = bb[i].name
        if not an == bn:
            raise Exception("Mismatch bone structure : idx={} '{}' '{}'".format(i, an, bn))

def mainproc():
    act = bpy.context.active_object
    if act == None:
        raise Exception('No active object')
    dst = getFirstNonActiveSelObject()
    if dst == None:
        raise Exception('No destination object')
    print("'{}' -> '{}'".format(act.name, dst.name))
    verifyIsValidArmature(act)
    verifyIsValidArmature(dst)
    verifyArmatureTopology(act, dst)
    syncBoneTrans(act, dst)

mainproc()
