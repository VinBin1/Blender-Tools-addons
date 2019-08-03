bl_info = {
    "name": "Sculpt Ready 3K Sphere",
    "author": "me",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Tool Shelf > Poly Sculpt",
    "description": "makes 3k sculpt ready sphere from cube",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
    }

import bpy


def main(context):
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 4
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


    bpy.ops.sculpt.sculptmode_toggle()
    bpy.ops.sculpt.dynamic_topology_toggle()
    bpy.context.scene.tool_settings.sculpt.detail_type_method = 'CONSTANT'
    bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True


class Dopoly(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "myops.add_dopoly"
    bl_label = "Cube to 3kpolysphere"


    def execute(self, context):
        main(context)
        return {'FINISHED'}

class PolyPanel(bpy.types.Panel):
    """Creates a Panel in the Tool Shelf"""
    bl_label = "Quick Polysphere"
    bl_idname = "OBJECT_PT_monkey"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Poly Sculpt"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("myops.add_dopoly")

def register():
    bpy.utils.register_class(Dopoly)
    bpy.utils.register_class(PolyPanel)

def unregister():
    bpy.utils.unregister_class(Dopoly)
    bpy.utils.unregister_class(PolyPanel)

if __name__ == "__main__":
    register()

  
