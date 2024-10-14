import bpy

context = bpy.context
obj = context.active_object
mesh = obj.data

def f(x):
    return 0.1 * (x ** 2)

for v in mesh.vertices:
    v.co[2] = f(v.co[1])
