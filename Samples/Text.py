import bpy

PI = 3.14159265359

def createText(loc, rad, rotDegZ, text):
    bpy.ops.object.text_add(enter_editmode=True, location=loc, radius=rad, rotation=(0, 0, rotZ * PI / 180.0))
    bpy.ops.font.delete(type='ALL')
    bpy.ops.font.text_insert(text=text)
    bpy.ops.object.editmode_toggle()
