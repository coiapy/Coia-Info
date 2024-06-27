bl_info = {
    "name": "Coia Info",
    "author": "Javier Aira",
    "version": (0,2,0),
    "blender": (2, 80, 0),
    "location": "VIEW_3D > Sidebar(UI) > Coia Info ",
    "description": "Operaciones en elementos de malla",
    "doc_url": "",
    "category": "3D View",
}

if "bpy" in locals():
    import importlib
    importlib.reload(funciones)
    importlib.reload(operadores)
    importlib.reload(panels)
    importlib.reload(mybpy)

else:
    from .funciones import *
    from .operadores import *
    from .panels import *
    from .mybpy import *

import bpy


class VarPropertyGroup(bpy.types.PropertyGroup):

    pp: bpy.props.IntProperty(name='') #portapapeles addon
    pptext: bpy.props.StringProperty(name='') #portapapeles addon 

    decimal_desliza: bpy.props.FloatProperty(name='ejeY', default= 0.0, precision=6)

    # Displacement
    cox: bpy.props.FloatProperty(name='X', default= 0, precision=6)
    coy: bpy.props.FloatProperty(name='Y', default= 0, precision=6)
    coz: bpy.props.FloatProperty(name='Z', default= 0, precision=6)

    # Coordenadas Locales vertice
    locx: bpy.props.FloatProperty(name='X', default= 0, precision=6)
    locy: bpy.props.FloatProperty(name='Y', default= 0, precision=6)
    locz: bpy.props.FloatProperty(name='Z', default= 0, precision=6)
    co_local: bpy.props.FloatVectorProperty(name='', precision=6)

    # Coordenadas Globales vertice
    gocx: bpy.props.FloatProperty(name='X', default= 0, precision=6)
    gocy: bpy.props.FloatProperty(name='Y', default= 0, precision=6)
    gocz: bpy.props.FloatProperty(name='Z', default= 0, precision=6)
    co_global: bpy.props.FloatVectorProperty(name='', precision=6)

    # Coordenadas Polares,Esfericas,Cilindricas, ...
    radius: bpy.props.FloatProperty(name='radio:',precision=6, default= 0)
    angle: bpy.props.FloatProperty(name='angle α:',precision=6, default= 0)
    angle_beta: bpy.props.FloatProperty(name='angle ß:',precision=6, default= 0)
    origen_mesh: bpy.props.FloatVectorProperty(name='')

    obj_activo: bpy.props.StringProperty(name='')

    vact: bpy.props.IntProperty(name='vertice')

    dist_2: bpy.props.FloatProperty(name='dist:', precision=6)

    vertice_a_distancia: bpy.props.FloatProperty(name='dist:',default= 0.3)

    mensaje: bpy.props.StringProperty(name='', default='Vert+press ↑')

    distancia_dos_puntos: bpy.props.StringProperty(name='',default='2 Vertices')
    vertice_activo: bpy.props.StringProperty(name='', default='Active')
    vertice_seleccionado: bpy.props.StringProperty(name='', default='Select')

    distancia_dos_puntos_int: bpy.props.FloatProperty(name='')
    vertice_seleccionado_int: bpy.props.IntProperty(name='')
    vertice_activo_int: bpy.props.IntProperty(name='')


    ajustar_distancia: bpy.props.FloatProperty(name='(d)', default= 0, precision=6)


    cursor_location: bpy.props.FloatVectorProperty(name='', precision=6)
    #bpy.data.scenes[bpy.context.scene.name].propiedades_p.cursor_location
    #bpy.context.scene.propiedades_p.cursor_location =

    bool_archivo: bpy.props.BoolProperty(name='Print to File: InfoCoor.txt', default=False)

    index_activo: bpy.props.IntProperty(name='')
    mensaje_end1: bpy.props.StringProperty(name='', default='')
    mensaje_end: bpy.props.StringProperty(name='', default='')

    factor: bpy.props.FloatProperty(name='', default= 1, precision=6)
    nueva_distancia: bpy.props.FloatProperty(name='')

    bool_f: bpy.props.BoolProperty(name='factor→', default=False)




    #bpy.context.scene.propiedades_p.mensaje_end1 = "I Need 1 Active Vertex"
    #bpy.data.scenes[bpy.context.scene.name].propiedades_p.mensaje_end = 'Worked !!!'


classes = (DefineOrientacion, EscalarMalla, OrigenACursor, DisolverLoop, CorteMallaDistancia, Subdividir, CorteMalla, AjustarDistancia, VIEW3D_PT_Coordinates, VarPropertyGroup, DistanciaDosPuntos, MoverVerticeActivo, VIEW3D_PT_Transform)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.propiedades_p = bpy.props.PointerProperty(type=VarPropertyGroup)


def unregister():
    del bpy.types.Scene.propiedades_p
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
