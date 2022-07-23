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

L =18 
jiaodu_qian = 45.0 /180.0 *3.1415926  # python transfer all into int if I use 45 rather than 45.0
bili_qian = 0.0

endPoint_qianzhong = CurvePointNorm(Curve("pressure"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
print(CurvePointNorm(Curve("pressure"), bili_qian))
# print('MXairfoil: debug: \n L*math.cos(jiaodu_qian)='+str(L*math.cos(jiaodu_qian)) +'\n jiaodu_qian')
print('MXairfoil: trying to get the start point. ')
print(endPoint_qianzhong)
polyline_qianzhong = new_polyline("polyline_qianzhong")
polyline_qianzhong.insert_point(1, CurvePointNorm(Curve("pressure"), bili_qian))
polyline_qianzhong.insert_point(2, endPoint_qianzhong)

endPoint_qianshang = CurvePointNorm(Curve("pressure2"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianshang = new_polyline("polyline_qianshang")
polyline_qianshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_qian))
polyline_qianshang.insert_point(2, endPoint_qianshang)

endPoint_qianxia = CurvePointNorm(Curve("pressure3"), bili_qian) - Point(L*math.cos(jiaodu_qian),L*math.sin(jiaodu_qian),0)
polyline_qianxia = new_polyline("polyline_qianxia")
polyline_qianxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_qian))
polyline_qianxia.insert_point(2, endPoint_qianxia)

bili_hou = 1 
jiaodu_hou = 15.0 /180.0 *3.1415926 

endPoint_houshang = CurvePointNorm(Curve("pressure2"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houshang = new_polyline("polyline_houshang")
polyline_houshang.insert_point(1, CurvePointNorm(Curve("pressure2"), bili_hou))
polyline_houshang.insert_point(2, endPoint_houshang)

endPoint_houzhong = CurvePointNorm(Curve("pressure"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houzhong = new_polyline("polyline_houzhong")
polyline_houzhong.insert_point(1, CurvePointNorm(Curve("pressure"), 1))
polyline_houzhong.move_point(1, CurvePointNorm(Curve("pressure"), 1))
polyline_houzhong.insert_point(2, endPoint_houzhong)

endPoint_houxia = CurvePointNorm(Curve("pressure3"), bili_hou) + Point(L*math.cos(jiaodu_hou),L*math.sin(jiaodu_hou),0)
polyline_houxia = new_polyline("polyline_houxia")
polyline_houxia.insert_point(1, CurvePointNorm(Curve("pressure3"), bili_hou))
polyline_houxia.insert_point(2, endPoint_houxia)