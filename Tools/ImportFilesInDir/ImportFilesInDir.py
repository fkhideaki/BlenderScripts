import glob
import bpy

def importOBJ(fn):
    bpy.ops.import_scene.obj(filepath=fn)

def getFilesInDir(dir, ext):
    files = glob.glob(dir + '\\*.' + ext)
    v = []
    for f in files:
        v.append(f)
    return v

def importFilesInDir(dir, ext):
    v = getFilesInDir(dir, ext)
    for f in v:
        if ext == 'obj':
            importOBJ(f)

#importFilesInDir(r'D:\ws\\_TMP\aaa\z', 'obj')
