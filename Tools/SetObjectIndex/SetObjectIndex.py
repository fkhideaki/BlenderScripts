import bpy

def getVisSelObjects():
    v = []
    for o in bpy.data.objects:
        if o.select_get() and o.visible_get():
            v.append(o)
    return v

def setAutoPassIndex():
    v = getVisSelObjects()
    i = 0
    for o in v:
        o.pass_index = i
        i += 1

setAutoPassIndex()
