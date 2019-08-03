import bpy

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subsurf"].levels = 4
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


bpy.ops.sculpt.sculptmode_toggle()
bpy.ops.sculpt.dynamic_topology_toggle()
bpy.context.scene.tool_settings.sculpt.detail_type_method = 'CONSTANT'
bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True
