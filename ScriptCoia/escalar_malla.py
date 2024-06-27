import bpy
import bmesh
from mathutils import Matrix, Vector

	
#bpy.ops.mesh.primitive_cube_add()

def aplica(verts):
	#bmesh.ops.translate(bm,vec=tr_vec,space=ref_frame,verts=verts)
	bmesh.ops.scale(bm,vec=scl_vec,space=ref_frame,verts=verts)
	return

bpy.ops.object.mode_set(mode='OBJECT')

me = bpy.context.object.data
bm = bmesh.new(use_operators=True)
bm.from_mesh(me)

ref_frame = Matrix.Identity(4)
#bm.faces.ensure_lookup_table()
#bm.edges.ensure_lookup_table()
bm.verts.ensure_lookup_table()	


f_check = bpy.context.scene.propiedades_p.bool_f
print("f_check", f_check)


if f_check ==True:
	f = bpy.context.scene.propiedades_p.factor
	print(f)

if f_check ==False:
	n_d = bpy.context.scene.propiedades_p.nueva_distancia
	d_2p = bpy.context.scene.propiedades_p.distancia_dos_puntos_int
	f = n_d/d_2p



#geometria = [vert for vert in bm.verts if vert.select] #vertices selec.
geometria = bm.verts[:] # All verts


#tr_vec = Vector((0.0, 0.0, 0.0))
scl_vec = Vector((f, f, f))
aplica(geometria)

bm.to_mesh(me)
bm.free()

bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.select_all(action='DESELECT')
