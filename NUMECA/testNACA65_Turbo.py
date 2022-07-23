mulu = 'C:/Users/y/Desktop/EnglishMulu/testNACA65'
beta=0.7854 # 45(90-45) degree.
# mulu = '.'
FT.create_project(mulu+"/testNACA65.iec")
FT.set_cyl_cart_configuration(0)
FT.select_output("_SD_YPLUS_")
FT.set_azimuthal_output_flag(0, 0)
FT.set_azimuthal_output_flag(3, 0)
FT.set_azimuthal_output_flag(46, 0)
FT.select_output("_ABSOLUTE_TOTAL_TEMPERATURE_")
FT.select_output("_ABSOLUTE_TOTAL_PRESSURE_")
FT.select_output("_TURB_WALL_DISTANCE_")
FT.set_azimuthal_output_flag(68, 0)
FT.link_mesh_file(mulu+"/testNACA65.igg", 0)
FT.set_unit_ratio(0.01)

#start set the configuration.
# FT.select_fluid_from_database("AIR", "Real Gas")
sudu = 41.148
FT.select_fluid_from_database("AIR(Perfect)", "Perfect Gas")
FT.set_mathematical_model(SPALART_ALLMARAS)
FT.set_tracer(0)
FT.set_harmonic_maximum_rank(1)
FT.set_preconditioning(1)
FT.set_reference_length(0.127)
FT.set_reference_velocity(sudu)

import math

#set bounndary condition.
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([124,2])
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([124,4])
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vz/|V|", 0)
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vr/|V|", math.cos(beta))
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vt/|V|", math.sin(beta))
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Absolute Total Pressure", 1.0108*101325)
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Absolute Total Temperature", 294)
# FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_parameter_value("Static Pressure", 101325)
# FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Turbulent Viscosity", 1e-7)

# FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_bc_type([25,10]) # outlet
# FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_parameter_value("Static Pressure", 101325)
FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_bc_type([27,40])
FT.get_bc_group(FT.get_bc_patch(0, 3, 0)).set_parameter_value("Static_Pressure", 91300)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([24,2])# inlet
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vx/|V|", 0.7071)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Vy/|V|", 0.7071)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Absolute Total Pressure", 1.0108*101325)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Turbulent Viscosity", 1e-5)

FT.set_user_solver_precision(1)
FT.select_output("_ABSOLUTE_TOTAL_TEMPERATURE_")
FT.select_output("_ABSOLUTE_TOTAL_PRESSURE_")

# this is to debug the uniformity 
import random
raodong = random.randint(0,300)
FT.set_nb_iter_max(3000+raodong) 

FT.get_initial_solution(0).set_velocity(Vector(sudu,0,0))
FT.get_initial_solution(0).set_coord_system("abs")
FT.get_initial_solution(0).set_flow_direction("J")
FT.get_initial_solution(1).set_coord_system("abs")
FT.get_initial_solution(1).set_velocity(Vector(sudu,0,0))
FT.get_initial_solution(2).set_coord_system("abs")
FT.get_initial_solution(2).set_velocity(Vector(sudu,0,0))
FT.get_initial_solution(2).set_flow_direction("Reverse J")
FT.get_initial_solution(1).set_flow_direction("J")
FT.save_selected_computations()