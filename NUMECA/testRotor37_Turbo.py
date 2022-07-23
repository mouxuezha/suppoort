mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor37'

# working='C:/Users/y/Desktop/EnglishMulu/PythonShishi/main/working/'
# saveDir = 'C:/Users/y/Desktop/EnglishMulu/NUMECAyanzheng/Rotor67shishi2/Result/Rotor67python'
# batshDir = 'C:/Users/y/Desktop/EnglishMulu/PythonShishi/main/'
working= mulu + '/FlowSetting'
saveDir = mulu + '/testRotor37.iec'
meshDir = mulu + '/Rotor37shishi.igg'

def get_theValue(working):
    # legacy code, get the value from configure file. It is not very ingenious.
    rotational_speed = open(working,'r')
    strBuffer= rotational_speed.read()
    value=float(strBuffer) 
    # value=int(strBuffer) 
    print('MXairfoil: get the value  '+strBuffer)
    print('in the dictionary: '+ working)
    return value 

FT.create_project(saveDir)
FT.set_user_solver_precision(1) # the change of percision must be bring forward to avoid warning.
FT.link_mesh_file(meshDir, 0)
FT.set_cyl_cart_configuration(1)

FT.set_unit_system(UNIT_DEFAULT)
FT.set_unit_ratio(0.01) # this is important to avoid negative density.
FT.select_fluid_from_database('AIR(Perfect)','Perfect Gas')

############################################################################
## set the flow Model
############################################################################
FT.set_time_configuration(STEADY)
FT.set_mathematical_model(SPALART_ALLMARAS)
FT.set_gravity_flag(0)
FT.set_reference_length( 0.25 )
FT.set_reference_velocity( 175 )
FT.set_reference_density( 1.205 )
FT.set_reference_temperature( 293 )
FT.set_reference_pressure( 101300.0 )

############################################################################
## set rotating machinary
############################################################################
zhuansu = get_theValue(working+"/rotational_speed.txt")
FT.get_rotating_block_group(0).set_rotational_speed(zhuansu)

############################################################################
## set boundary condition
############################################################################
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_bc_type([124,4])
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_parameter_value("Absolute Total Pressure", [4,[[0.179222,99947,0],[0.18349,101740,0],[0.187452,101872,0],[0.191414,101872,0],[0.195682,101872,0],[0.199644,101872,0],[0.205435,101872,0],[0.210922,101872,0],[0.216713,101811,0],[0.222504,101740,0],[0.22799,101670,0],[0.232258,101740,0],[0.23622,101811,0],[0.240182,101740,0],[0.24445,101528,0],[0.248412,100910,0],[0.251765,98913.5,0],[0.254203,95600.1,0]]])
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_parameter_value("Absolute Total Temperature", [4,[[0.179222,288.265,0],[0.18349,287.862,0],[0.187452,287.775,0],[0.191414,287.804,0],[0.195682,287.804,0],[0.199644,287.804,0],[0.205435,287.862,0],[0.210922,287.977,0],[0.216713,288.035,0],[0.222504,288.265,0],[0.22799,288.381,0],[0.232258,288.323,0],[0.23622,288.208,0],[0.240182,288.15,0],[0.24445,288.208,0],[0.248412,288.265,0],[0.251765,288.265,0],[0.254203,288.381,0]]])

yali = get_theValue(working+"/Static_Pressure.txt")
FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_bc_type([125,10])
FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Radius", 0.22)
FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static_Pressure", yali)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([113,1])
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Rotational Speed 1", 0)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Rotational Speed 2", -17188)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Higher Radius Limit", 1)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Lower Axial Limit", -0.005)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Higher Axial Limit", 0.05)
FT.set_MG_flag(0)
FT.set_MG_flag(1)

FT.get_initial_solution(0).set_turbo_patch_pressure("INLET", "row_1_flux_1_Main_Blade_upStream_inlet", 90000)

FT.set_azimuthal_output_flag(0, 1)
FT.set_azimuthal_output_flag(3, 1)
FT.set_azimuthal_output_flag(46, 1)
FT.select_output("_ABSOLUTE_TOTAL_TEMPERATURE_")
FT.select_output("_ABSOLUTE_TOTAL_PRESSURE_")
FT.set_azimuthal_output_flag(2, 1)
FT.set_azimuthal_output_flag(5, 1)
FT.set_azimuthal_output_flag(9, 1)
FT.select_output("_TURB_WALL_DISTANCE_")
FT.select_output("_SD_YPLUS_")
FT.set_azimuthal_output_flag(68, 1)
FT.select_output("_RELATIVE_TOTAL_TEMPERATURE_")
FT.select_output("_RELATIVE_TOTAL_PRESSURE_")
FT.select_output("_SD_STATIC_PRESSURE_")
FT.select_output("_SD_STATIC_TEMPERATURE_")
FT.select_output("_SD_SKIN_FRICTION_")
FT.set_output_writing_frequency(50)
FT.set_nb_iter_max(700)

FT.save_project()
FT.save_selected_computations() #project must saved before save computation, or it will hard to find.
# what a fucking silly system. the .run file have to be saved seperately.

# FT.save_project()
