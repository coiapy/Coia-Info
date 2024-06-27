import bpy
import bmesh
import math

"""
from importlib import reload
import mybpy
reload(mybpy)
from mybpy import *
"""

C = bpy.context
D = bpy.data
O = bpy.ops

#---------------------------------------------#

def vert_activo():
    O.object.mode_set(mode='EDIT')
    me = C.edit_object.data
    bm = bmesh.from_edit_mesh(me)
    vact = bm.select_history.active.index
    ea = escena_activa()
    D.scenes[ea].propiedades_p.vact = vact
    return vact

def vert_activo_coordenadas():
    O.object.mode_set(mode='EDIT')
    me = C.edit_object.data
    bm = bmesh.from_edit_mesh(me)
    vact = bm.select_history.active.index
    return bm.verts[vact].co

def verts_seleccionados():
    datos = C.active_object.data.vertices
    vse = [v for v in datos if v.select]
    verts_sel=[]
    for i in vse:
        verts_sel.append(i.index)    
    return verts_sel

def verts_seleccionados_sin_activo():
    datos = C.active_object.data.vertices
    vse = [v for v in datos if v.select]
    verts_sel=[]
    for i in vse:
        verts_sel.append(i.index)
    va = vert_activo()
    verts_sel.remove(va)
    return verts_sel 

#---------------------------------------------#

def obj_activo_nombre():
    return C.object.name

def obj_activo():
    return C.active_object

def obj_modo():
    return C.object.mode

def obj_edicion():
    return C.edit_object.name

def objs_seleccionados():
    return C.selected_objects

def obj_vert():
    '''Retorna tupla objeto, vertice activo ('Cubo.002', 2)'''
    obj_act = C.active_object
    ver_act = vert_activo()
    return (obj_act.name, ver_act.numerator)

def obj_modo_almacen():
    current_mode = bpy.context.object.mode
    return current_mode

#---------------------------------------------#

def escena_activa():
    return C.scene.name

def cursor_localizacion():
    '''Retorna vector'''
    ea = escena_activa()
    cl = D.scenes[ea].cursor.location
    mensaje_end(str(cl))
    return cl #vector

def dist_2_ptos():
    '''Distancia entre 2 puntos
    Para funcionar objeto y malla tienen el mismo nombre'''

    bpy.ops.object.mode_set(mode='OBJECT')

    obj = bpy.context.active_object.name # mesh active
    v_all = bpy.data.meshes[obj].vertices # list with all vertices
    vselect = [] # crea lista vacia o reinicia

    for i in v_all:
        if i.select == True:
            vselect.append(i)

    if len(vselect)==2:

        dd = (vselect[0].co.xyz - vselect[1].co.xyz)
        dis = math.sqrt(dd[0]**2+dd[1]**2+dd[2]**2) #float

        bpy.ops.object.mode_set(mode='EDIT')

        tdas = str(vselect[0].index)
        tdzs = str(vselect[1].index)

        print (f"Distancia vertices: {tdas}->{tdzs} : {dis}")

        bpy.context.scene.propiedades_p.dist_2 = dis

    if len(vselect)!=2:
        
        bpy.ops.object.mode_set(mode='EDIT')

    #mesh_act.update_from_editmode()
    return dis

def triedro():
    '''Dibuja triedrotrirectangulo desde posicion cursor'''

    cl = bpy.context.scene.cursor.location

    def dibuja_triedro(x,y,z):
            bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(x,y,z), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "proportional_size":1})

    def ini():
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=True,location=(0,0,cl.z))
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.merge(type='CENTER')      

    def remove():
        bpy.ops.mesh.remove_doubles(threshold=0.00001, use_unselected=True) 
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.object.editmode_toggle()

    def draw(self, context):
        self.layout.label(text = '(0,0,0)?')

    if cl.z>=0:
        if cl.x!=0:
            if cl.y!=0:
                ini()
                dibuja_triedro(cl.x,0,0); dibuja_triedro(0,0,-cl.z); dibuja_triedro(0,cl.y,0)
                dibuja_triedro(-cl.x,0,0); dibuja_triedro(0,0,cl.z); dibuja_triedro(0,-cl.y,0)
                remove()

    if cl.z<0:
        ini()
        dibuja_triedro(cl.x,0,0); dibuja_triedro(0,0,-cl.z); dibuja_triedro(0,cl.y,0)
        dibuja_triedro(-cl.x,0,0); dibuja_triedro(0,0,cl.z); dibuja_triedro(0,-cl.y,0)
        remove()

    if cl.z==0:
        if cl.x==0:
            if cl.y==0:
                bpy.context.window_manager.popup_menu(draw, title="Triedrotrirectangulo", icon='INFO')

    return

def orientacion_define():
    '''Define orientacion Coia_orient a partir de vertices selecionados,
    deseleciona y queda vertice activo como único selecionado'''

    #No funciona en consola, (revisar)

    me = bpy.context.edit_object.data
    bm = bmesh.from_edit_mesh(me)


    vselect = []
    for v in bm.verts:
        if v.select == True:
            vselect.append(v)


    if len(vselect)>=2:

        bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)

        vact = bm.select_history.active.index

        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.vertices[vact].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')

    return

def refresh():
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    return

def mensaje_end(msn='---'):
    bpy.context.scene.propiedades_p.mensaje_end = msn
    return


#---------------------------------------------#

"""
def ver_propiedades():
    pass
    esc = escena_activa()
    esc.[propiedades_p]
    return


D.scenes["Escena"].transform_orientation_slots[0].type
O.transform.create_orientation(name="mueveV", use=True, overwrite=True)


#Lista de Grupos de Propiedades
D.scenes['Scene']['

#Lista de Propiedades usadas (no sólo definidas)
D.scenes['Scene']['propiedades_p']['

#Vertice activo (almacenado)
D.scenes['Scene']['propiedades_p']['vact']
"""
"""
def vert_activo_mover(): #######.....########
    # vert_activo_mover(eje='z', valor=3.0):
    '''
    obj = C.active_object.name
    v_todos = D.meshes[obj].vertices
    O.object.mode_set(mode='OBJECT')

    va = verts_seleccionados()

    O.mesh.select_all(action='DESELECT')

    v_todos[va].select = True
    v_todos[va].co.z += 1.0
    '''
    '''
    me = C.edit_object.data
    bm = bmesh.from_edit_mesh(me)

    vselect = []
    for v in bm.verts:
        if v.select == True:
            vselect.append(v)

    vact = bm.select_history.active.index

    O.object.mode_set(mode = 'OBJECT')
    obj = C.active_object
    O.object.mode_set(mode = 'EDIT') 
    O.mesh.select_mode(type="VERT")
    O.mesh.select_all(action = 'DESELECT')
    O.object.mode_set(mode = 'OBJECT')
    obj.data.vertices[vact].select = True
    O.object.mode_set(mode = 'EDIT')
    '''

    xx = D.scenes["Scene"].propiedades_p.cox
    yy = D.scenes["Scene"].propiedades_p.coy
    zz = D.scenes["Scene"].propiedades_p.coz

    O.transform.translate(value=(xx, yy, zz))


    #O.transform.translate(value=(0, yy, 0), orient_axis_ortho='X', orient_type='mueveV')


    '''
    O.object.mode_set(mode='OBJECT')
    command = f'D.meshes[obj].verts[-1].co.{eje}+={valor}'
    print(command)
    command
    
    #obj_activo().update_from_editmode()
    '''
    return
"""
