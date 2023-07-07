import bpy


def addNewCollection(name):
    c = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(c)
    return c

def moveObjectToCollection(collection, obj):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    collection.objects.link(obj)
