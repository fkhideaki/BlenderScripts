import bpy

def getContextArea(areaName):
    for area in bpy.context.screen.areas:
        if area.type == areaName:
            return area
    raise RuntimeError('Area not found (' + name + ')')

def getRegion(area, regionName):
    for region in area.regions:
        if region.type == regionName:
            return region
    raise RuntimeError('Region not found in area ' + area.type + ' (' + regionName + ')')

def getOverride3D():
    area = getContextArea('VIEW_3D')
    region = getRegion(area, 'WINDOW')
    override = {'area': area, 'region': region}
    return override

cont = getOverride3D()
bpy.ops.transform.rotate(cont, value=1.5708, axis=(0, 0, 1))
