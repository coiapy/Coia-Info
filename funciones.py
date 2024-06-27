import bpy
import pathlib
import sys
import bmesh
from mathutils import Vector


script_path = __file__
script_dir = pathlib.Path(script_path).resolve().parent
# print(f"[pathlib] script_dir -> {script_dir}")

sys.path.append(str(script_dir))


def mueve_v(self, context):
    file = (f'{script_dir}/ScriptCoia/mueve_v.py')
    bpy.ops.script.python_file_run(filepath=file)


def malla(self, context):
    file = (f'{script_dir}/ScriptCoia/malla.py')
    bpy.ops.script.python_file_run(filepath=file)
    self.report({'INFO'}, "The custom operator actually worked!")


def d_o():
    '''Define Orientacion'''
    me = bpy.context.edit_object.data
    bm = bmesh.from_edit_mesh(me)

    vselect = []
    for v in bm.verts:
        if v.select == True:
            vselect.append(v)


    if len(vselect)>=2:

        bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)
        bm.free()
        return


    #if len(vselect)<2:
    else:
        bm.free()
        return


def corte_malla(punto_cursor=(0,0,0)):
    '''Si el objeto esta rotado aplicar antes la transformacion'''

    vector_loc = bpy.context.object.location

    bpy.ops.object.mode_set(mode='OBJECT')
    me = bpy.context.object.data
    bm = bmesh.new(use_operators=True)
    bm.from_mesh(me)
    #------------------------- C O D E -------------------------#
    selected_faces = [face for face in bm.faces if face.select]

    if len(selected_faces)==1:

        punto_cursor_modify = punto_cursor - vector_loc

        face_sel= selected_faces[0].index

        plane_no = bpy.context.active_object.data.polygons[face_sel].normal
        print("plane_no:", type(plane_no))

        bmesh.ops.bisect_plane(bm, 
        geom= bm.verts[:] + bm.edges[:] + bm.faces[:],
        dist=0.000000001,
        plane_co = punto_cursor_modify,
        plane_no = plane_no,
        use_snap_center=False, 
        clear_outer=False,
        clear_inner=False,
        )
        #------------------------- C O D E -------------------------#
        bm.to_mesh(me)
        bm.free()
        bpy.ops.object.editmode_toggle()
        bpy.context.scene.propiedades_p.mensaje_end = "Worked !!!"
        return

    else:
        bm.free()
        bpy.ops.object.editmode_toggle()
        bpy.context.scene.propiedades_p.mensaje_end = "Select A Face To Make ││ Cut !!!"
        return


def corte_malla_distancia(punto_cursor=(0,0,0)):

    scene = bpy.context.scene.name
    obj_act = bpy.context.active_object

    dis = bpy.context.scene.propiedades_p.distancia_dos_puntos_int
    v_sel = bpy.context.scene.propiedades_p.vertice_seleccionado_int
    v_act = bpy.context.scene.propiedades_p.vertice_activo_int

    bpy.ops.view3d.snap_cursor_to_active()
    #Lee propiedad
    dis_ajuste = bpy.context.scene.propiedades_p.ajustar_distancia

 
    bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)

    coo_local = obj_act.data.vertices[v_act].co
    coo_global = obj_act.matrix_world @ obj_act.data.vertices[v_act].co

    ################################################################
    #Operacion Cursor
    co = bpy.data.scenes[scene].cursor.location
    y = bpy.data.scenes[scene].cursor.location[1]


    #coordenadas de vertice activo
    coor_vert_act = obj_act.data.vertices[v_act].co


    #########################

    bpy.ops.transform.translate(value=(0, dis_ajuste, 0), orient_type='Coia_orient')
    bpy.ops.view3d.snap_cursor_to_active()
    bpy.ops.transform.translate(value=(0, -dis_ajuste, 0), orient_type='Coia_orient')

    bpy.ops.mesh.select_all(action='DESELECT')

    # modo seleccion
    bpy.ops.mesh.select_mode(type='FACE')


    #Hasta aqui coloca el cursor en punto de corte y deja con:
    # vertices activo y sel y con orientacion local
    # faltaria deseleccionar todo y selec cara paralela y
    #corte_malla()

    return


    #########################

    #Ajuste de coordenadas???
    #resultante = coor_vert_act + Vector((0,dis_ajuste,0))
  

    #coo_global = obj_act.matrix_world @ obj_act.data.vertices[v_act].co


    #bpy.data.scenes[scene].cursor.location = coo_global



    #bpy.ops.transform.translate(value=(0, dis_ajuste , 0), orient_type='Coia_orient', orient_matrix_type='Coia_orient')

    # cambiar co.y posicion de cursor segun dis_ajuste


    #bpy.data.scene.cursor.location.xyz = lo_cu
    #ver indices
    #bpy.context.space_data.overlay.show_extra_indices = True
    print ('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')

    return



def origen_a_cursor():

    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()

    return
