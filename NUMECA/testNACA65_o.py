mulu = 'C:/Users/y/Desktop/EnglishMulu/testNACA65'
# mulu = '.'
close_project()
set_project_configuration("2D", 2)
set_project_header("I G G", "Interactive Geometry Modeling and", "Grid Generation System")
import_data_file(mulu + "/pressure.dat")
import_data_file(mulu + "/suction.dat")
import_data_file(mulu + "/suction2.dat")
import_data_file(mulu + "/pressure2.dat")
import_data_file(mulu + "/suction3.dat")
import_data_file(mulu + "/pressure3.dat")



import math

L = 0.5
jiaodu_qian = 45.0 /180.0 *3.1415926  # python transfer all into int if I use 45 rather than 45.0
bili_qian = 0.0
jvli_sigma = 12.7 

endPoint_qianzhong = CurvePointNorm(Curve("pressure"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
print(CurvePointNorm(Curve("pressure"), bili_qian))
# print('MXairfoil: debug: \n L*math.cos(jiaodu_qian)='+str(L*math.cos(jiaodu_qian)) +'\n jiaodu_qian')
print('MXairfoil: trying to get the start point. ')
print(endPoint_qianzhong)
o_qianzhong = new_polyline("o_qianzhong")
o_qianzhong.insert_point(1, CurvePointNorm(Curve("pressure"), bili_qian))
o_qianzhong.insert_point(2, endPoint_qianzhong)

endPoint_qianshang = CurvePointNorm(Curve("pressure2"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
o_qianshang = new_polyline("o_qianshang")
o_qianshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_qian))
o_qianshang.insert_point(2, endPoint_qianshang)

endPoint_qianxia = CurvePointNorm(Curve("pressure3"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
o_qianxia = new_polyline("o_qianxia")
o_qianxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_qian))
o_qianxia.insert_point(2, endPoint_qianxia)

bili_hou = 1 
jiaodu_hou = 15.0 /180.0 *3.1415926 

endPoint_houshang = CurvePointNorm(Curve("pressure2"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
o_houshang = new_polyline("o_houshang")
o_houshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_hou))
o_houshang.insert_point(2, endPoint_houshang)

endPoint_houzhong = CurvePointNorm(Curve("pressure"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
o_houzhong = new_polyline("o_houzhong")
o_houzhong.insert_point(1, CurvePointNorm(Curve("pressure"), 1))
o_houzhong.move_point(1, CurvePointNorm(Curve("pressure"), 1))
o_houzhong.insert_point(2, endPoint_houzhong)

endPoint_houxia = CurvePointNorm(Curve("pressure3"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
o_houxia = new_polyline("o_houxia")
o_houxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_hou))
o_houxia.insert_point(2, endPoint_houxia)

# then add Cspiles for O-H mesh.
cspline_shang = new_cspline("cspline_shang")
cspline_shang.insert_point(1, CurvePointNorm(o_qianshang, 1))
cspline_shang.move_point(1, CurvePointNorm(o_qianshang, 1))
P2_o_shang = CurvePointNorm(o_qianshang, 1) + Point(0.4,-0.2,0)
cspline_shang.insert_point(2, P2_o_shang)

for i in range(6):
    bili_i = 0.1 + 0.17*i 
    Pi_o_shang =CurvePointNorm(Curve("pressure2"), bili_i) + Point(0.4,-0.4,0)
    cspline_shang.insert_point(3+i, Pi_o_shang)

Pjian1_o_shang = CurvePointNorm(o_houshang, 1) + Point(-0.05,-0.2,0)
cspline_shang.insert_point(3+i+1, Pjian1_o_shang)
# polyline_debug = new_polyline("polyline_debug")
# polyline_debug.insert_point(1, CurvePointNorm(Curve("pressure"), 0))
# polyline_debug.insert_point(2, Pi_o_shang)
cspline_shang.insert_point(3+i+2, CurvePointNorm(o_houshang, 1))

# then add Cspiles for O-H mesh. suction side.
cspline_zhong = new_cspline("cspline_zhong")
cspline_zhong.insert_point(1, CurvePointNorm(o_qianzhong, 1))
cspline_zhong.move_point(1, CurvePointNorm(o_qianzhong, 1))
P2_o_zhong = CurvePointNorm(o_qianzhong, 1) + Point(-0.1,0.2,0)
cspline_zhong.insert_point(2, P2_o_zhong)

for i in range(6):
    bili_i = 0.1 + 0.17*i 
    Pi_o_zhong =CurvePointNorm(Curve("suction"), bili_i) + Point(-0.4,+0.4,0)
    cspline_zhong.insert_point(3+i, Pi_o_zhong)

Pjian1_o_zhong = CurvePointNorm(o_houzhong, 1) + Point(-0.15,+0.2,0)
cspline_zhong.insert_point(3+i+1, Pjian1_o_zhong)
# polyline_debug = new_polyline("polyline_debug")
# polyline_debug.insert_point(1, CurvePointNorm(Curve("pressure"), 0))
# polyline_debug.insert_point(2, Pi_o_shang)
cspline_zhong.insert_point(3+i+2, CurvePointNorm(o_houzhong, 1))


# then, plot the H mesh as done before.
L =12 
jiaodu_qian = 45.0 /180.0 *3.1415926  # python transfer all into int if I use 45 rather than 45.0

endPoint_qianzhong = CurvePointNorm(o_qianzhong, 1) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianzhong = new_polyline("polyline_qianzhong")
polyline_qianzhong.insert_point(1, CurvePointNorm(o_qianzhong, 1))
polyline_qianzhong.insert_point(2, endPoint_qianzhong)

endPoint_qianshang = CurvePointNorm(o_qianshang, 1) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianshang = new_polyline("polyline_qianshang")
polyline_qianshang.insert_point(1, CurvePointNorm(o_qianshang, 1))
polyline_qianshang.insert_point(2, endPoint_qianshang)

endPoint_qianxia = CurvePointNorm(o_qianxia, 1) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianxia = new_polyline("polyline_qianxia")
polyline_qianxia.insert_point(1, CurvePointNorm(o_qianxia, 1) )
polyline_qianxia.insert_point(2, endPoint_qianxia)

bili_hou = 1 
jiaodu_hou = 15.0 /180.0 *3.1415926 

endPoint_houshang = CurvePointNorm(o_houshang, 1) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houshang = new_polyline("polyline_houshang")
polyline_houshang.insert_point(1, CurvePointNorm(o_houshang, 1))
polyline_houshang.insert_point(2, endPoint_houshang)

endPoint_houzhong = CurvePointNorm(o_houzhong, 1) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houzhong = new_polyline("polyline_houzhong")
polyline_houzhong.insert_point(1, CurvePointNorm(o_houzhong, 1) )
polyline_houzhong.insert_point(2, endPoint_houzhong)

endPoint_houxia = CurvePointNorm(o_houxia, 1) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houxia = new_polyline("polyline_houxia")
polyline_houxia.insert_point(1, CurvePointNorm(o_houxia, 1))
polyline_houxia.insert_point(2, endPoint_houxia)

# then create blocks. this is big one.
new_block_face(Point(-8.63135528564453, 4.5818395614624, 0), Point(-8.63135528564453, 1.16852641105652, 0), Point(-1.08887243270874, 1.16852641105652, 0), Point(-1.08887243270874, 4.5818395614624, 0)) # these parameter have no meaning.
# block("Block_1").set_size(85, 241, 2, 1)

total_y = 161 #81 161
bianhua = 5 #0 30
cut = 33 + bianhua
cut2 = total_y-36 -bianhua

total_x = 261 #501 261
bianhua = 0 #50 0
d1 = 41 +bianhua
d2 = total_x-68-bianhua # 173 for total_x = 241
block("Block_1").set_size(total_y, total_x, 2, 1)
# set the shangmian 
segment("Block_1", 1, 3, 1).cluster_end(0.05)
move_vertex(vertex("Block_1", 1, 1, 1), CurvePointNorm(polyline_qianshang, 1))
move_vertex(vertex("Block_1", 1, 1, 2), CurvePointNorm(polyline_qianzhong, 1))
move_vertex(vertex("Block_1", 1, 2, 1), CurvePointNorm(polyline_houshang, 1))
move_vertex(vertex("Block_1", 1, 2, 2), CurvePointNorm(polyline_houzhong, 1))
edge("Block_1", 1, 3).insert_vertex(0.3)
move_vertex(vertex("Block_1", 1, 3, 2), CurvePointNorm(polyline_qianshang, 0))
edge("Block_1", 1, 3).insert_vertex(0.7)
move_vertex(vertex("Block_1", 1, 3, 3), CurvePointNorm(polyline_houshang, 0))
edge("Block_1", 1, 3).insert_vertex(0.5)
move_vertex(vertex("Block_1", 1, 3, 3), CurvePointNorm(cspline_shang, 0.5))
vertex("Block_1", 1, 3, 2).attach_fix_point()
vertex("Block_1", 1, 3, 4).attach_fix_point()

fixed_point("Block_1", 1, 3, 1).change_index(d1, edge("Block_1", 1, 3))
fixed_point("Block_1", 1, 3, 2).change_index(d2, edge("Block_1", 1, 3))

# set the xiamian
edge("Block_1", 1, 4).insert_vertex(0.3)
move_vertex(vertex("Block_1", 1, 4, 2), CurvePointNorm(polyline_qianzhong, 0))
edge("Block_1", 1, 4).insert_vertex(0.7)
move_vertex(vertex("Block_1", 1, 4, 3), CurvePointNorm(polyline_houzhong, 0))
edge("Block_1", 1, 4).insert_vertex(0.5)
move_vertex(vertex("Block_1", 1, 4, 3), CurvePointNorm(cspline_zhong, 0.5))
vertex("Block_1", 1, 4, 2).attach_fix_point()
vertex("Block_1", 1, 4, 4).attach_fix_point()
fixed_point("Block_1", 1, 4, 1).change_index(d1, edge("Block_1", 1, 4))
fixed_point("Block_1", 1, 4, 2).change_index(d2, edge("Block_1", 1, 4))



#add a piont to ajust the mesh
face("Block_1", 1).create_grid_point(cut, d2)
edge("Block_1", 1, 5).create_curve("Block_1_1_5")
face("Block_1", 1).create_grid_point(cut, d1)
face("Block_1", 1).create_grid_point(cut2, d1)
edge("Block_1", 1, 8).create_curve("Block_1_1_8")

# polyline_m_shang = new_polyline("polyline_m_shang")
# polyline_m_shang.insert_point(1, CurvePointNorm(Curve("Block_1_1_5"), 0.29))
# polyline_m_shang.insert_point(2, CurvePointNorm(Curve("Block_1_1_5"), 0.71))
# move_vertex(vertex("Block_1", 1, 7, 2), CurvePointNorm(polyline_m_shang, 0))
# move_vertex(vertex("Block_1", 1, 6, 2), CurvePointNorm(polyline_m_shang, 1))

# polyline_m_zhong = new_polyline("polyline_m_zhong")
# polyline_m_zhong.insert_point(1, CurvePointNorm(Curve("Block_1_1_8"), 0.22))
# polyline_m_zhong.insert_point(2, CurvePointNorm(Curve("Block_1_1_8"), 0.71))
# move_vertex(vertex("Block_1", 1, 8, 2), CurvePointNorm(polyline_m_zhong, 0))
# move_vertex(vertex("Block_1", 1, 8, 3), CurvePointNorm(polyline_m_zhong, 1))

# jixu xiu
m1 = 0.29 #zuoshang, for 5
m2 = 0.71 #youshang 
m3 = 0.23 # for 8
m4 = 0.71
P_m2_zhong =CurvePointNorm(Curve("Block_1_1_8"), 0.5)+  Point(-0.1,0.1,0) 
# P_m2_zhong = CurvePointNorm(polyline_m_zhong, 0.5) *0.2 +  CurvePointNorm(Curve("Block_1_1_8"), 0.5) * 0.8 + Point(-0.1,0.1,0) 

cspline_m2_zhong = new_cspline("cspline_m2_zhong")
cspline_m2_zhong.insert_point(1, CurvePointNorm(Curve("Block_1_1_8"), m3))
cspline_m2_zhong.insert_point(2,P_m2_zhong)
cspline_m2_zhong.insert_point(3, CurvePointNorm(Curve("Block_1_1_8"), m4))
edge("Block_1", 1, 8).insert_vertex(0.5)
move_vertex(vertex("Block_1", 1, 8, 3), CurvePointNorm(cspline_m2_zhong, 0.5))

cspline_qian_shu = new_cspline("cspline_qian_shu")
cspline_qian_shu.insert_point(1, CurvePointNorm(polyline_qianshang, 0))
cspline_qian_shu.insert_point(2, CurvePointNorm(Curve("Block_1_1_5"), m1))
cspline_qian_shu.insert_point(3, CurvePointNorm(Curve("Block_1_1_8"), m3))
cspline_qian_shu.insert_point(4, CurvePointNorm(polyline_qianzhong, 0))
move_vertex(vertex("Block_1", 1, 7, 2), CurvePointNorm(cspline_qian_shu, 0.29))
move_vertex(vertex("Block_1", 1, 8, 2), CurvePointNorm(cspline_m2_zhong, 0))

cspline_hou_shu = new_cspline("cspline_hou_shu")
cspline_hou_shu.insert_point(1, CurvePointNorm(polyline_houshang, 0))
cspline_hou_shu.insert_point(2, CurvePointNorm(Curve("Block_1_1_5"), m2))
cspline_hou_shu.insert_point(3, CurvePointNorm(Curve("Block_1_1_8"), m4))
cspline_hou_shu.insert_point(4, CurvePointNorm(polyline_houzhong, 0))
move_vertex(vertex("Block_1", 1, 6, 2), CurvePointNorm(cspline_hou_shu, 0.25))
move_vertex(vertex("Block_1", 1, 8, 4), CurvePointNorm(cspline_m2_zhong, 1))

# then mesh the O part.
total_i_o = int((50.0/4)*4+1)
total_j_o = int(round((d2-d1)/4)*4+1)
print(total_j_o)
new_block_face(Point(3.39499855041504, 0.861613750457764, 0), Point(3.39499855041504, -0.436336040496826, 0), Point(5.27523708343506, -0.436336040496826, 0), Point(5.27523708343506, 0.861613750457764, 0))
move_vertex(vertex("Block_2", 1, 1, 1), CurvePointNorm(polyline_qianzhong, 0))
move_vertex(vertex("Block_2", 1, 2, 1), CurvePointNorm(polyline_houzhong, 0))
move_vertex(vertex("Block_2", 1, 1, 2), CurvePointNorm(Curve("pressure"), 0))
move_vertex(vertex("Block_2", 1, 2, 2), CurvePointNorm(Curve("pressure"), 1))
edge("Block_2", 1, 4).insert_vertex(0.5)
move_vertex(vertex("Block_2", 1, 4, 2), CurvePointNorm(Curve("suction"), 0.5))
block("Block_2").set_size(total_i_o, total_j_o, 2, 1)

# clustering_group("wall").add_segment(segment("Block_1", 1, 4, 2), 0)
# clustering_group("wall").add_segment(segment("Block_2", 1, 3, 1), 0)
# clustering_group("wall").add_segment(segment("Block_2", 1, 4, 1), 0)

new_block_face(Point(-6.87801647186279, 18.5406627655029, 0), Point(-6.87801647186279, 16.8179588317871, 0), Point(-3.82894706726074, 16.8179588317871, 0), Point(-3.82894706726074, 18.5406627655029, 0))
block("Block_3").set_size(total_i_o, total_j_o, 2, 1)
move_vertex(vertex("Block_3", 1, 1, 1), CurvePointNorm(polyline_houshang, 0))
move_vertex(vertex("Block_3", 1, 2, 1), CurvePointNorm(polyline_qianshang, 0))
move_vertex(vertex("Block_3", 1, 2, 2), CurvePointNorm(Curve("pressure2"), 0))
move_vertex(vertex("Block_3", 1, 1, 2), CurvePointNorm(Curve("pressure2"), 1))
edge("Block_3", 1, 4).insert_vertex(0.5)
move_vertex(vertex("Block_3", 1, 4, 2), CurvePointNorm(Curve("pressure2"), 0.5))

# move_vertex(vertex("Block_3", 1, 2,1), CurvePointNorm(Curve("pressure2"), 0))
# move_vertex(vertex("Block_3", 1, 2, 2), CurvePointNorm(Curve("pressure2"), 1))
# move_vertex(vertex("Block_3", 1, 1,2), CurvePointNorm(polyline_houshang, 0))
# move_vertex(vertex("Block_3", 1, 1, 1), CurvePointNorm(polyline_qianshang, 0))
# edge("Block_3", 1, 4).insert_vertex(0.5)
# move_vertex(vertex("Block_3", 1, 4, 2), CurvePointNorm(Curve("pressure2"), 0.5))
# edge("Block_3", 1, 3).insert_vertex(0.5)
# move_vertex(vertex("Block_3", 1, 3, 2), CurvePointNorm(cspline_shang, 0.5))


#distribution of mesh.
create_clustering_group("layer")
clustering_group("layer").add_segment(segment("Block_3", 1, 1, 1), 0)
clustering_group("layer").add_segment(segment("Block_2", 1, 1, 1), 0)
clustering_group("layer").add_segment(segment("Block_2", 1, 2, 1), 0)
clustering_group("layer").add_segment(segment("Block_3", 1, 2, 1), 0)

create_clustering_group("qian")
clustering_group("qian").add_segment(segment("Block_1", 1, 3, 1), 0)
clustering_group("qian").add_segment(segment("Block_1", 1, 4, 1), 0)
clustering_group("qian").add_segment(segment("Block_1", 1, 5, 1), 0)
clustering_group("qian").add_segment(segment("Block_1", 1, 8, 1), 0)
create_clustering_group("hou")
clustering_group("hou").add_segment(segment("Block_1", 1, 3, 3), 0)
clustering_group("hou").add_segment(segment("Block_1", 1, 4, 3), 0)
clustering_group("hou").add_segment(segment("Block_1", 1, 5, 3), 0)
clustering_group("hou").add_segment(segment("Block_1", 1, 8, 3), 0)
create_clustering_group("heng")
clustering_group("heng").add_segment(segment("Block_1", 1, 3, 2), 0)
clustering_group("heng").add_segment(segment("Block_1", 1, 4, 2), 0)
create_clustering_group("heng2")
clustering_group("heng2").add_segment(segment("Block_3", 1, 3, 1), 0)
clustering_group("heng2").add_segment(segment("Block_2", 1, 3, 1), 0)
create_clustering_group("wall")
clustering_group("wall").add_segment(segment("Block_2", 1, 4, 1), 0)
clustering_group("wall").add_segment(segment("Block_3", 1, 4, 1), 0)
# clustering_group("wall").add_segment(segment("Block_3", 1, 3, 1), 0)
# clustering_group("wall").add_segment(segment("Block_2", 1, 3, 1), 0)
create_clustering_group("wall2")# they have different dirrection.
clustering_group("wall2").add_segment(segment("Block_3", 1, 4, 1), 0)

create_clustering_group("jian")
# clustering_group("jian").add_segment(segment("Block_1", 1, 3, 1), 0)
clustering_group("jian").add_segment(segment("Block_1", 1, 5, 1), 0)
clustering_group("jian").add_segment(segment("Block_1", 1, 5, 2), 0)

clustering_group("qian").cluster_end(0.1)
clustering_group("hou").cluster_start(0.1)
clustering_group("heng").cluster_both_ends2(0.03, 0.03, 0)
clustering_group("heng2").cluster_both_ends2(0.03, 0.03, 0)
# clustering_group("heng2").cluster_start(0.05)
# clustering_group("heng").cluster_start(0.05)
clustering_group("wall").cluster_both_ends2(0.015, 0.005, 0)
clustering_group("wall2").cluster_both_ends2(0.005, 0.015, 0)
clustering_group("jian").cluster_end(0.1)
clustering_group("layer").cluster_end(0.00077) # 0.00077 is for y+=1, since O-H is here, it can be good.

#then boundary condition.
block_by_face_extrusion_comb(face("Block_1", 1), Vector(0, 0, 3.54680514335632), 0, Point(0, 0, 0), 0, 0, 0, 0)
patch("Block_1", 5, 1).divide_by_range(Range(1, d1, 1, 2))
patch("Block_1", 5, 2).divide_by_range(Range(d1, d2, 1, 2))
patch("Block_1", 6, 1).divide_by_range(Range(1, d1, 1, 2))
patch("Block_1", 6, 2).divide_by_range(Range(d1, d2, 1, 2))
set_repetition_all_blocks("TRANSLATION", 2, Vector(0, jvli_sigma, 0)) # setting the julv here or it will GG. Geometry-Periordicity in GUI
block_by_face_extrusion_comb(face("Block_1", 1), Vector(0, 0, 3.54680514335632), 0, Point(0, 0, 0), 0, 0, 0, 0)
connect_patches(patch("Block_1", 5, 1), patch("Block_1", 6, 1), "IHIGH", "JHIGH", "PER", 1E-005)
connect_patches(patch("Block_1", 5, 3), patch("Block_1", 6, 3), "IHIGH", "JHIGH", "PER", 1E-005)
connect_patches(patch("Block_2", 3, 1), patch("Block_3", 4, 1), "IHIGH", "JHIGH", "PER", 1E-005)
connect_patches(patch("Block_2", 4, 1), patch("Block_3", 3, 1), "IHIGH", "JHIGH", "PER", 1E-005)
search_connections(1E-005)
patch("Block_1", 3, 1).set_type("INL")
patch("Block_1", 4, 1).set_type("OUT")
patch("Block_2", 6, 1).set_type("SOL")
patch("Block_3", 6, 1).set_type("SOL")

save_project("./testNACA65.igg")