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
