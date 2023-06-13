import bpy
import math
import os
import os.path


def ToggleEditmode():
	bpy.ops.object.editmode_toggle()


def GetMeshByName(name):
    return bpy.data.meshes[name]

def GetMeshByIdx(idx):
	return bpy.data.meshes[idx]

def GetMeshObjectByName(name):
    for obj in bpy.data.objects:
        if obj.type!="MESH":
            continue
        if obj.name != name:
            continue
        return obj
    return None
    
def GetMeshByObjectName(name):
    obj = GetMeshObjectByName(name)
    if obj == None:
        return None
    return obj.data

def PrintMeshNames():
    for m in bpy.data.meshes:
        print(m.name)

def PrintObjectNames():
    for o in bpy.data.objects:
        print(o.name)


def OpenObj(filename):
    bpy.ops.import_scene.obj(filepath=filename)


def PrintTextNames():
    for t in bpy.data.texts:
        print(t.name)

def PlotAllTexts():
    for t in bpy.data.texts:
        print("----------------[begin]----------------")
        print(t.name)
        for l in t.lines:
           print(l.body)
        print("----------------[end]----------------")
        print("")


def currentDirPath(fname):
    cdir = os.path.abspath(__file__)
    cdir = os.path.dirname(cdir)
    cdir = os.path.dirname(cdir)
    if (cdir[1:] == ':\\'):
        raise Exception('no current dir')
    return cdir + '\\' + fname

def getCurrentDir():
    return currentDirPath('')


dir toggleConsole():
    bpy.ops.wm.console_toggle()


def setActiveObject(obj):
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

def setActiveObjectByName(name):
    obj = bpy.data.objects[name]
    if not obj:
        return
    setActiveObject(obj)

def addNewCollection():
    c = bpy.data.collections.new('')
    bpy.context.scene.collection.children.link(c)
    return c

def moveObjectToCollection(collection, obj):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    collection.objects.link(obj)


def getSels():
    sels = []
    for o in bpy.data.objects:
        if o.select_get() and o.visible_get():
            sels.append(o)
    return sels

def getTargetSD():
    sels = getSels()
    if len(sels) != 2:
        return None, None
    act = bpy.context.active_object
    if sels[0] is act:
        return act, sels[1]
    if sels[1] is act:
        return act, sels[0]
    return None, None
