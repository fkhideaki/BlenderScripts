import bpy

bl_info = {
    "name" : "Clothsim ext Plugin",
    "author" : "Hideaki Fukushima",
    "version" : (0, 1),
    "blender" : (2, 6, 5),
    "location" : "",
    "description" : "Cloth simulation helper plugin",
    "warning" : "",
    "wiki_url" : "",
    "tracker_url" : "",
    "category" : ""
}


def toMeshMode():
    bpy.ops.object.mode_set(mode = 'EDIT_MESH')

def toObjectMode():
    bpy.ops.object.mode_set(mode = 'OBJECT')

def getAllSelectedObj():
    sels = []
    for obj in bpy.data.objects:
        if obj.select:
            sels.append(obj)
    return sels

def getOrCreateSeamGroup(obj):
    vgName = 'CLOTHSIM_SEAM'
    ai = 0
    for vg in obj.vertex_groups:
        if vg.name == vgName:
            obj.vertex_groups.active_index = ai
            return vg
        ai = ai + 1
    obj.vertex_groups.new(name = vgName)
    obj.vertex_groups.active_index = ai
    return obj.vertex_groups[vgName]


class CLEX_OP_SeamBridge(bpy.types.Operator):
    bl_idname = "object.clex_seam_bridge"
    bl_label = "Seam Bridge"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        toMeshMode()
        obj = context.object
        bpy.ops.mesh.bridge_edge_loops()
        vg = getOrCreateSeamGroup(obj)
        bpy.ops.object.vertex_group_assign()
        bpy.ops.mesh.delete(type='ONLY_FACE')
        return {'FINISHED'}

class CLEX_OP_SeamStrip(bpy.types.Operator):
    bl_idname = "object.clex_seam_strip"
    bl_label = "Seam Strip"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        toMeshMode()
        obj = context.object
        vg = getOrCreateSeamGroup(obj)
        bpy.ops.object.vertex_group_assign()
        bpy.ops.mesh.delete(type='ONLY_FACE')
        return {'FINISHED'}

def setAllSelClothAttrib(toCloth):
    toObjectMode()
    sels = getAllSelectedObj()
    pre_act = bpy.context.scene.objects.active
    bpy.ops.object.select_all(action='DESELECT')
    for obj in sels:
       bpy.context.scene.objects.active = obj
       if toCloth:
           bpy.ops.object.modifier_add(type='CLOTH')
       else:
           bpy.ops.object.modifier_remove(modifier="Cloth")
    for obj in sels:
       obj.select = True
    bpy.context.scene.objects.active = pre_act

class CLEX_OP_ToCloth(bpy.types.Operator):
    bl_idname = "object.clex_to_cloth"
    bl_label = "To Cloth"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        setAllSelClothAttrib(True)
        return {'FINISHED'}

class CLEX_OP_ResetCloth(bpy.types.Operator):
    bl_idname = "object.clex_reset_cloth"
    bl_label = "Reset Cloth"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        setAllSelClothAttrib(False)
        return {'FINISHED'}

class ClothExtPanel(bpy.types.Panel):
    bl_category = "ClothExt"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "TOOLS"
    bl_label = "ClothExt"

    def draw(self, context):
        layout = self.layout
        view = context.space_data

        col = layout.column(align=True)
        col.label(text="Seam:")
        row = col.row()
        row.operator("object.clex_seam_bridge")
        row = col.row()
        row.operator("object.clex_seam_strip")

        col = layout.column(align=True)
        col.label(text="Cloth:")
        row = col.row()
        row.operator("object.clex_to_cloth")
        row = col.row()
        row.operator("object.clex_reset_cloth")


def register():
    bpy.utils.register_class(CLEX_OP_ResetCloth)
    bpy.utils.register_class(CLEX_OP_ToCloth)
    bpy.utils.register_class(CLEX_OP_SeamBridge)
    bpy.utils.register_class(CLEX_OP_SeamStrip)
    bpy.utils.register_class(ClothExtPanel)

def unregister():
    bpy.utils.unregister_class(CLEX_OP_ResetCloth)
    bpy.utils.unregister_class(CLEX_OP_ToCloth)
    bpy.utils.unregister_class(CLEX_OP_SeamBridge)
    bpy.utils.unregister_class(CLEX_OP_SeamStrip)
    bpy.utils.unregister_class(ClothExtPanel)


if __name__ == "__main__":
    register()
