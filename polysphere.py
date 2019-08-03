import bpy

bl_info = {
    "name": "cube test addon",
    "author": "Mee",
    "version": (1, 0, 0),
    "blender": (2, 79, 0),
    "location": "View3D",
    "description": "simple panel add cube",
    "category": "Development",
}

def main(context):
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subsurf"].levels = 4
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")


    bpy.ops.sculpt.sculptmode_toggle()
    bpy.ops.sculpt.dynamic_topology_toggle()
    bpy.context.scene.tool_settings.sculpt.detail_type_method = 'CONSTANT'
    bpy.context.scene.tool_settings.sculpt.use_smooth_shading = True
    
class ASimpleToolClass(bpy.types.Panel):

    bl_label="Polysphere Tools"
    bl_idname=" me button"
    bl_space_type='VIEW_3D'
    bl_regiontype='WINDOW'
    bl_region_type='TOOLS'
    
    bl_context = 'objectmode'
    bl_category='MyTools' 
    
    
    def draw(self, context):
        layout=self.layout
        layout.operator('py.ops.object.dothis() ' ,text='make Polyspher 3k')
            
         
   def execute(self, context):
        main(context)
        return {'FINISHED'}

  
    
def register():
    bpy.utils.register_class(ASimpleToolClass)
    

def unregister():
    bpy.utils.unregister_class(ASimpleToolClass)
    
    

if __name__ == "__main__":
    register()
            

        
