import bpy


def assignMaterial(obj, materialName):
    mesh = obj.data
    mat = bpy.data.materials[materialName]
    mesh.materials.clear()
    mesh.materials.append(mat)
