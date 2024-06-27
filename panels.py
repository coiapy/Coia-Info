import bpy


class VIEW3D_PT_Coordinates(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Coia Info'
    bl_label = 'Coordinates'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        ps = context.scene.propiedades_p
        layout.label(text='Coming Soon', icon='MONKEY')


class VIEW3D_PT_Transform(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Coia Info'
    bl_label = 'Transform' 
    #bl_context = 'objectmode' # Indica en que modo se mostrara
    #bl_options = {'DEFAULT_CLOSED'}
    #bl_order = 1 (nº mas bajo da prioridad, se ordena antes) 

    def draw(self, context):
        layout = self.layout
        ps = context.scene.propiedades_p

        #Define orientacion

        layout.label(text='EditMode+Sel.≥2 Vert', icon='REC')

        split = layout.split(factor=0.4, align=True)
        split.label(text='Define:')
        split.operator('coia.define_orientacion',text='NewOrient', icon='ORIENTATION_LOCAL')
        

        # Orientation selecciona
        split = layout.split(factor=0.4, align=True)
        split.label(text='Ó Selec.:')
        orient_slot = context.scene.transform_orientation_slots[0]
        split.prop_with_popover(orient_slot,"type",text="",panel="VIEW3D_PT_transform_orientations")
        

        #Desplazamiento
        layout.label(text='Desplazamiento:')
        col = layout.column(align=True)
        col.prop(ps, 'cox')
        col.prop(ps, 'coy')
        col.prop(ps, 'coz')

        #Mover Seleccionados
        col.operator('coia.mover_vertice_activo',icon='VIEW_PAN', text='Mover Selec. !!!')


        #⚫ Distance (Precision µm)
        layout.label(text='Distance.Precis≡µm', icon='REC')
        subrow = layout.row(align=True)
        subrow.operator('coia.distancia_dos_puntos', text = '•←?→•', icon='DRIVER_DISTANCE')
        subrow.prop(ps,'distancia_dos_puntos')
        #Ajust Distance 2 vertices
        #layout.label(text='Ajustar Distancia 2 Vertices', icon='REC')
        subrow = layout.row(align=True)
        subrow.operator('coia.ajustar_distancia',text='•←d→•',icon='DRIVER_DISTANCE')
        subrow.prop(ps,'ajustar_distancia',text="d")


        #⚫ Escalar Malla
        layout.label(text='Config. Escalar Malla', icon='REC')

        subrow = layout.row(align=True)
        subrow.prop(ps,'bool_f')
        subrow.prop(ps,'factor', text='f')
        layout.prop(ps,'nueva_distancia', text='New(d)')
        layout.operator('coia.escalar_malla',icon='FULLSCREEN_EXIT', text='Escalar Malla !!!')

        
        #⚫ Utiles
        layout.label(text='Utiles:', icon='REC')

        subrow = layout.row(align=True)
        subrow.operator('coia.subdivide', text='─•─ Subdi.')
        subrow.operator('view3d.snap_cursor_to_active', text='Cur→Act', icon='CURSOR')
       
        subrow = layout.row(align=True)
        subrow.operator('coia.disolver_loop',text='→▓▓←')
        subrow.operator("coia.origen_a_cursor", icon='TRANSFORM_ORIGINS', text='Org→Cur')
      
        #Seleccionar geometria
        #layout.label(text='Seleccionar Geometría', icon='REC')
        #layout.operator('coia.seleccionar_geometria',text='─(──)───')


        #⚫ Cortar Malla
        layout.label(text='Config. Cortar Malla', icon='REC')

        split = layout.split(factor=0.4, align=True)
        split.prop(ps,'vertice_activo', text='Act')
        split.prop(ps,'ajustar_distancia',text="")

        layout.operator('coia.corte_malla_distancia', icon='CURSOR', text='←d→• Situar Cursor')

        #split = layout.split(factor=0.1, align=True)
        #split.label(text='▓←')
        #split.operator('coia.corte_malla', icon='CURSOR', text='→▓ Cortar Malla')
        

        #Selec. Cara Paralela a Corte +
        box = layout.box()
        box.label(text='[Con Cara // a Corte Selec.]')
        box.operator('coia.corte_malla',text='▓↔▓ Cortar Malla !!!')

        #layout.separator()

        subrow = layout.row(align=True)
        subrow.prop(ps,'vertice_seleccionado')
        subrow.label(text=' Sel.|Act.')
        subrow.prop(ps,'vertice_activo')

        layout.prop(ps,'mensaje_end',text='', icon='INFO')
        #bpy.context.scene.propiedades_p.mensaje_end = "Worked !!!"

        #•▓←d→•|▓ ▒ ↑↓ → ← ─ ↔ • µ≡ ± ≥ ≤ 
