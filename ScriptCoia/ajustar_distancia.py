# AutoSave !!!

import bpy
import bmesh
import math


def ajustar_distancia():
    scene = bpy.context.scene.name

    bpy.ops.object.mode_set(mode='OBJECT')
    me = bpy.context.object.data # Optener malla activa
    bm = bmesh.new(use_operators=True) # Crear un BMesh vacío.
    bm.from_mesh(me) # Copiar desde la malla

    selected_verts = [vert for vert in bm.verts if vert.select]

    if len(selected_verts)!=2:
        bm.free()
        bpy.ops.object.editmode_toggle()
        bpy.context.scene.propiedades_p.mensaje_end = "Select '2' Vertices !!!"
        return


    if len(selected_verts)==2:
        vert_activo = bm.select_history.active

        if vert_activo in selected_verts:
            vvv = bm.select_history.active.index
            dd = (selected_verts[0].co.xyz - selected_verts[1].co.xyz)
            dis = math.sqrt(dd[0]**2+dd[1]**2+dd[2]**2) #float
            selected_verts.remove(vert_activo)


        else:
            bm.free()
            bpy.ops.object.editmode_toggle()
            bpy.context.scene.propiedades_p.mensaje_end = "I Need 1 Active Vertex"
            return

        dis_new = bpy.context.scene.propiedades_p.ajustar_distancia
        print("dis_new", dis_new)
        dis_ajuste = dis_new - dis
        print("dis_ajuste", dis_ajuste)

        bm.to_mesh(me)
        bm.free()
        bpy.ops.object.editmode_toggle()

        bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)

        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.vertices[vvv].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')

        bpy.ops.transform.translate(value=(0, dis_ajuste , 0), orient_type='Coia_orient', orient_matrix_type='Coia_orient', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        return


ajustar_distancia()
