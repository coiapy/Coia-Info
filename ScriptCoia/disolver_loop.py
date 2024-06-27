import bpy

bpy.ops.transform.edge_slide(value=-1, mirror=True, correct_uv=True)
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles()
bpy.ops.mesh.select_all(action='DESELECT')
