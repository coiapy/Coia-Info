import bpy
import pathlib
from .funciones import *
from .mybpy import *


script_path = __file__
script_dir = pathlib.Path(script_path).resolve().parent

"""
class VerticeADistancia(bpy.types.Operator):
    bl_idname = "coia.vertice_a_distancia"
    bl_label = "vertice a una distancia"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/vertice_a_distancia.py')
        bpy.ops.script.python_file_run(filepath=file)
        self.report({'INFO'}, "The custom operator actually worked!")
        return {'FINISHED'}


class CoordenadasVerticeActivo(bpy.types.Operator):
    '''Info Vertice Activo'''
    bl_idname = "coia.coordenadas_vertice_activo"
    bl_label = "Coordenadas vertice activo"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/coordenadas_vertice_activo.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}

"""
class DefineOrientacion(bpy.types.Operator):#••
    '''Seleccionar 2 o mas vertices -> define nueva orientacion (Coia_orient) -> la usa
    El vertice activo (último select) será el origen de los nuevos ejes'''
    bl_idname = "coia.define_orientacion"
    bl_label = "Define Orientacion a partir de 2 vetices o mas"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/define_orientacion.py')
        bpy.ops.script.python_file_run(filepath=file)
        #self.report({'INFO'}, "Worked!")
        return {'FINISHED'}

"""
class MueveVertice(bpy.types.Operator):
    '''mueve_v'''
    bl_idname = "coia.mueve_v"
    bl_label = "Mueve vertice en borde"

    def execute(self, context):
        mueve_v(self, context)
        return {'FINISHED'}


class OperaDistancia(bpy.types.Operator):
    '''OperaDistancia'''
    bl_idname = "coia.dist_2"
    bl_label = "Info distancia entre dos vertices"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/dist_2.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}
"""

class DistanciaDosPuntos(bpy.types.Operator):#••
    '''• Distancia entre dos vertices seleccionados'''
    bl_idname = "coia.distancia_dos_puntos"
    bl_label = "Distancia entre dos puntos"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/distancia_dos_puntos.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}


class MoverVerticeActivo(bpy.types.Operator):#••
    '''• Toma valores incrementales de distancia de XYZ y 
    Desplaza Seleccionados según Orientacion Activa '''
    bl_idname = 'coia.mover_vertice_activo'  
    bl_label = 'mover vertice activo'
 
    def execute(self, context):
        orientacion = bpy.data.scenes["Scene"].transform_orientation_slots[0].type
        props = self.properties 
        scene = context.scene 
        bpy.ops.transform.translate(value=(scene.propiedades_p.cox, scene.propiedades_p.coy, scene.propiedades_p.coz), orient_type=orientacion)
        return {'FINISHED'}

"""
class Malla(bpy.types.Operator):
    '''Malla'''
    bl_idname = "coia.malla"
    bl_label = "malla"

    def execute(self, context):
        malla(self, context)
        return {'FINISHED'}
"""

class AjustarDistancia(bpy.types.Operator):#••
    '''•Ajusta Distancia (d) entre dos vertices.
    Mueve activo en direccion a seleccionado.'''
    bl_idname = "coia.ajustar_distancia"
    bl_label = "Ajusta Distancia entre dos puntos"

    def execute(self, context):
        d_o() #Define orientacion
        file = (f'{script_dir}/ScriptCoia/ajustar_distancia.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}


class CorteMalla(bpy.types.Operator):#••
    '''• Corte en Malla por localizacion de Cursor
    paralelo a Cara Seleccionada .'''
    bl_idname = "coia.corte_malla"
    bl_label = "Corta Malla ..."

    def execute(self, context):
        c_loc = bpy.data.scenes[bpy.context.scene.name].cursor.location
        bpy.data.scenes[bpy.context.scene.name].propiedades_p.cursor_location = c_loc 
        corte_malla(c_loc)
        return {'FINISHED'} 


class CorteMallaDistancia(bpy.types.Operator):#••
    '''• Situa Cursor entre vertice activo y seleccionado
    a distancia (d) del vertice activo '''
    bl_idname = "coia.corte_malla_distancia"
    bl_label = "Corta Malla a distancia d de vertice activo"

    def execute(self, context):
        c_loc = bpy.data.scenes[bpy.context.scene.name].cursor.location
        bpy.data.scenes[bpy.context.scene.name].propiedades_p.cursor_location = c_loc

        #Distancia a variables: distancia_dos_puntos y distancia_dos_puntos_int
        file = (f'{script_dir}/ScriptCoia/distancia_dos_puntos.py')
        bpy.ops.script.python_file_run(filepath=file)

        #Crea orientacion #################### necesario??
        bpy.ops.transform.create_orientation(name="Coia_orient", use=True, overwrite=True)

        #Actualiza 'phytonicamente'
        bpy.ops.object.editmode_toggle(); bpy.ops.object.editmode_toggle()

        corte_malla_distancia(c_loc)

        return {'FINISHED'}


class Subdividir(bpy.types.Operator):#••
    '''• Subdivide Lado/Edge en el Punto Medio'''
    bl_idname = "coia.subdivide"
    bl_label = "Subdivide ..."

    def execute(self, context):
        bpy.ops.mesh.subdivide()
        return {'FINISHED'}


class DisolverLoop(bpy.types.Operator):#••
    '''• Disolver loop interior (bordes y vertices) seleccionado'''
    bl_idname = "coia.disolver_loop"
    bl_label = "Disolver loop interior seleccionado"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/disolver_loop.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}


class OrigenACursor(bpy.types.Operator):#••
    '''• Origen a Cursor'''
    bl_idname = "coia.origen_a_cursor"
    bl_label = "Origen a cursor"

    def execute(self, context):
        origen_a_cursor()
        return {'FINISHED'}


class EscalarMalla(bpy.types.Operator):#••
    '''• Escala Malla'''
    bl_idname = "coia.escalar_malla"
    bl_label = "Escala Malla"

    def execute(self, context):
        file = (f'{script_dir}/ScriptCoia/escalar_malla.py')
        bpy.ops.script.python_file_run(filepath=file)
        return {'FINISHED'}








