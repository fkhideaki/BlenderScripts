bl_info = {
    'name': 'Coord adulst',
    'author': 'Hideaki Fukushima',
    'version': (1, 0, 0),
    'blender': (2, 65, 0),
    'location': 'View3D > Properties panel > Mesh Display tab (edit-mode)',
    'warning': '',
    'description': 'Adjust object coordinate and unit scale',
    'wiki_url': '',
    'tracker_url': '',
    'category': '3D View'}


import bpy
import cmath
import bgl
import blf
import mathutils
import bmesh

def rotMain(ax, ay, az, ang):
    cx = (ax == 1)
    cy = (ay == 1)
    cz = (az == 1)
    bpy.ops.transform.rotate(
        value=cmath.pi * 0.5 * ang,
        axis=(ax, ay, az),
        constraint_axis=(cx, cy, cz),
        constraint_orientation='GLOBAL',
        mirror=False, proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1)

def rotYZXMain(dir):
    n = cmath.sqrt(3.0).real
    ang = cmath.pi * dir *2.0 / 3.0
    bpy.ops.transform.rotate(
        value=ang,
        axis=(n, n, n),
        constraint_axis=(False, False, False),
        constraint_orientation='GLOBAL',
        mirror=False, proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0)

def scaleMain(s):
    bpy.ops.transform.resize(
        value=(s, s, s),
        constraint_axis=(False, False, False),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1)

class Rot90PX(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_px"
    bl_label = "X+"
    def execute(self, context):
        rotMain(1, 0, 0, 1.0)
        return {'FINISHED'}

class Rot90MX(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_mx"
    bl_label = "X-"
    def execute(self, context):
        rotMain(1, 0, 0, -1.0)
        return {'FINISHED'}

class Rot90PY(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_py"
    bl_label = "Y+"
    def execute(self, context):
        rotMain(0, 1, 0, 1.0)
        return {'FINISHED'}

class Rot90MY(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_my"
    bl_label = "Y-"
    def execute(self, context):
        rotMain(0, 1, 0, -1.0)
        return {'FINISHED'}

class Rot90PZ(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_pz"
    bl_label = "Z+"
    def execute(self, context):
        rotMain(0, 0, 1, 1.0)
        return {'FINISHED'}

class Rot90MZ(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot90_mz"
    bl_label = "Z-"
    def execute(self, context):
        rotMain(0, 0, 1, -1.0)
        return {'FINISHED'}

class RotYZX(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot_yzx"
    bl_label = "yzx"
    def execute(self, context):
        rotYZXMain(1.0)
        return {'FINISHED'}

class RotZXY(bpy.types.Operator):
    bl_idname = "object.coordadjust_rot_zxy"
    bl_label = "zxy"
    def execute(self, context):
        rotYZXMain(-1.0)
        return {'FINISHED'}

class Scale10P(bpy.types.Operator):
    bl_idname = "object.coordadjust_scale_10p"
    bl_label = "*10"
    def execute(self, context):
        scaleMain(10.0)
        return {'FINISHED'}

class Scale10M(bpy.types.Operator):
    bl_idname = "object.coordadjust_scale_10m"
    bl_label = "/10"
    def execute(self, context):
        scaleMain(1.0 / 10.0)
        return {'FINISHED'}

class Rot90Panel(bpy.types.Panel):
    """Adjust objects coordination"""
    bl_label = "CoordAdjust"
    bl_idname = "OBJECT_PT_COORD_ADJUST"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        row = layout.row(align=True)
        row.operator("object.coordadjust_rot90_px", text="X+")
        row.operator("object.coordadjust_rot90_py", text="Y+")
        row.operator("object.coordadjust_rot90_pz", text="Z+")

        row = layout.row(align=True)
        row.operator("object.coordadjust_rot90_mx", text="X-")
        row.operator("object.coordadjust_rot90_my", text="Y-")
        row.operator("object.coordadjust_rot90_mz", text="Z-")

        row = layout.row(align=True)
        row.operator("object.coordadjust_rot_yzx", text="yzx")
        row.operator("object.coordadjust_rot_zxy", text="zxy")

        row = layout.row(align=True)
        row.operator("object.coordadjust_scale_10p", text="*10")
        row.operator("object.coordadjust_scale_10m", text="/10")

def register():
    bpy.utils.register_class(Rot90PX)
    bpy.utils.register_class(Rot90MX)
    bpy.utils.register_class(Rot90PY)
    bpy.utils.register_class(Rot90MY)
    bpy.utils.register_class(Rot90PZ)
    bpy.utils.register_class(Rot90MZ)
    bpy.utils.register_class(RotYZX)
    bpy.utils.register_class(RotZXY)
    bpy.utils.register_class(Scale10P)
    bpy.utils.register_class(Scale10M)
    bpy.utils.register_class(Rot90Panel)

def unregister():
    bpy.utils.unregister_class(Rot90PX)
    bpy.utils.unregister_class(Rot90MX)
    bpy.utils.unregister_class(Rot90PY)
    bpy.utils.unregister_class(Rot90MY)
    bpy.utils.unregister_class(Rot90PZ)
    bpy.utils.unregister_class(Rot90MZ)
    bpy.utils.unregister_class(RotYZX)
    bpy.utils.unregister_class(RotZXY)
    bpy.utils.unregister_class(Scale10P)
    bpy.utils.unregister_class(Scale10M)
    bpy.utils.unregister_class(Rot90Panel)

if __name__ == "__main__":
    register()
