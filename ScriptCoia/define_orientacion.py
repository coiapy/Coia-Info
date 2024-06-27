import bpy
import bmesh


obj = bpy.context.view_layer.objects.active
if all([bool(obj), obj.type == "MESH", obj.mode == "EDIT"]):

    mesh_act = bpy.context.active_object #New
    me = bpy.context.edit_object.data
    bm = bmesh.from_edit_mesh(me)


    vselect = []
    for v in bm.verts:
        if v.select == True:
            vselect.append(v)


    if len(vselect)>=2:

        bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)
        mesh_act.update_from_editmode() #New
        vact = bm.select_history.active.index

        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.vertices[vact].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')


        bpy.data.scenes[bpy.context.scene.name].propiedades_p.vertice_seleccionado = str(vact)
        bpy.data.scenes[bpy.context.scene.name].propiedades_p.vertice_activo =  'None'
        bm.free()

        #bpy.context.space_data.overlay.show_extra_indices = True
        #bpy.context.space_data.show_gizmo_object_translate = True
        bpy.data.scenes[bpy.context.scene.name].propiedades_p.mensaje_end = ""

else:
    bpy.data.scenes[bpy.context.scene.name].propiedades_p.mensaje_end = "EditMode+Select ≥2 Vert"


