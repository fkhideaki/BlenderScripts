import bpy


def addNewCollection():
    c = bpy.data.collections.new('')
    bpy.context.scene.collection.children.link(c)
    return c

def moveObjectToCollection(collection, obj):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    collection.objects.link(obj)
