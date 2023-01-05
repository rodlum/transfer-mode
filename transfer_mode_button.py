import bpy

class TransferModeButton(bpy.types.Operator):
    """Transfer mode button"""
    bl_idname = "object.transfer_mode_button"
    bl_label = "Transfer Mode"

    def execute(self, context):
        bpy.ops.object.transfer_mode()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(TransferModeButton)

def unregister():
    bpy.utils.unregister_class(TransferModeButton)

if __name__ == "__main__":
    register()
