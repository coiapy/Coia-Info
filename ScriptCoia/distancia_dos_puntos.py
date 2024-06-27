import bpy
import bmesh
import math

def distancia_dos_puntos(): 

    bpy.ops.object.mode_set(mode='OBJECT')
    me = bpy.context.object.data # Optener malla activa
    bm = bmesh.new(use_operators=True) # Crear un BMesh vacío.
    bm.from_mesh(me) # Copiar desde la mallala

    selected_verts = [vert for vert in bm.verts if vert.select]

    if len(selected_verts)!=2:
        bm.free()
        bpy.ops.object.editmode_toggle()
        bpy.context.scene.propiedades_p.mensaje_end = "Select '2' Vert Or 1 Edge !!!"
        return


    if len(selected_verts)==2:
        vert_activo = bm.select_history.active

        if vert_activo in selected_verts:
            dd = (selected_verts[0].co.xyz - selected_verts[1].co.xyz)
            dis = math.sqrt(dd[0]**2+dd[1]**2+dd[2]**2) #float
            selected_verts.remove(vert_activo)

            bpy.context.scene.propiedades_p.distancia_dos_puntos_int = dis
            bpy.context.scene.propiedades_p.vertice_seleccionado_int = selected_verts[0].index 
            bpy.context.scene.propiedades_p.vertice_activo_int = vert_activo.index

            bpy.context.scene.propiedades_p.vertice_activo = str(vert_activo.index)
            bpy.context.scene.propiedades_p.vertice_seleccionado = str(selected_verts[0].index)
            bpy.context.scene.propiedades_p.distancia_dos_puntos = str(round(dis, 6))
            bpy.context.scene.propiedades_p.mensaje_end = 'Worked !!!'
            
        else:
            dd = (selected_verts[0].co.xyz - selected_verts[1].co.xyz)
            dis = math.sqrt(dd[0]**2+dd[1]**2+dd[2]**2) #float
            sel = []
            for i in selected_verts: sel.append(i.index)
        
            bpy.context.scene.propiedades_p.vertice_activo = 'None'
            bpy.context.scene.propiedades_p.vertice_seleccionado = str(sel)
            bpy.context.scene.propiedades_p.distancia_dos_puntos = str(round(dis, 6))
            bpy.context.scene.propiedades_p.mensaje_end = 'Worked !!!'



    bm.free()
    bpy.ops.object.editmode_toggle()
    return dis


distancia_dos_puntos()
