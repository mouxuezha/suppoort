mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'

# working='C:/Users/y/Desktop/EnglishMulu/PythonShishi/main/working/'
# saveDir = 'C:/Users/y/Desktop/EnglishMulu/NUMECAyanzheng/Rotor67shishi2/Result/Rotor67python'
# batshDir = 'C:/Users/y/Desktop/EnglishMulu/PythonShishi/main/'
working= mulu + '/Turbo_set'
saveDir = mulu + '/testRotor67.iec'
meshDir = mulu + '/testRotor67.igg'

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
print("MXairfoil: calculate project established in numeca")
FT.set_user_solver_precision(1) # the change of percision must be bring forward to avoid warning.
# FT.link_mesh_file('C:/Users/y/Desktop/EnglishMulu/NUMECAyanzheng/Rotor67shishi2/Result/shishi-1-stage.igg',1)
FT.link_mesh_file(meshDir,0)
	
FT.set_cyl_cart_configuration(1)
	
# FT.set_computation_name(0, "000_shishi")
FT.set_unit_system(UNIT_DEFAULT)
FT.set_unit_ratio(0.01) # this is important to avoid negative density.
FT.select_fluid_from_database('AIR(Perfect)','Perfect Gas')

############################################################################
## set the flow Model
############################################################################
FT.set_time_configuration(STEADY)
FT.set_mathematical_model(SPALART_ALLMARAS)
FT.set_gravity_flag(0)
FT.set_reference_length( 0.35 )
FT.set_reference_velocity( 200 )
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
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_bc_type([124,2])
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_bc_type([124,4])
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_parameter_value("Absolute Total Pressure", [4,[[0.095174,95843.3175,0],[0.097028,98183.925,0],[0.098882,99835.5225,0],[0.100736,100798.11,0],[0.110084,101355.3975,0],[0.129591,101426.325,0],[0.147396,101426.325,0],[0.164414,101355.3975,0],[0.180645,101426.325,0],[0.196469,101355.3975,0],[0.211988,101355.3975,0],[0.226873,101355.3975,0],[0.234798,101284.47,0],[0.24257,101142.615,0],[0.249758,99359.295,0],[0.25113,98325.78,0],[0.252501,96957.8925,0],[0.253848,94617.285,0],[0.255194,92144.955,0]]])
FT.get_bc_group(FT.get_bc_patch(2, 1, 0)).set_parameter_value("Absolute Total Temperature", [4,[[0.095174,288.524595,0],[0.097028,288.524595,0],[0.098882,288.697485,0],[0.100736,288.524595,0],[0.110084,287.97711,0],[0.129591,287.97711,0],[0.147396,288.26526,0],[0.164414,287.97711,0],[0.180645,287.97711,0],[0.196469,287.97711,0],[0.211988,288.15,0],[0.226873,288.43815,0],[0.234798,288.38052,0],[0.24257,288.43815,0],[0.249758,288.49578,0],[0.25113,288.43815,0],[0.252501,288.524595,0],[0.253848,287.86185,0],[0.255194,288.49578,0]]])

# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static Pressure", [4,[[0.133299,107282.91,0],[0.146126,111072.465,0],[0.158902,114932.9475,0],[0.171526,117628.1925,0],[0.183847,119826.945,0],[0.196164,121833.18,0],[0.20828,123413.85,0],[0.22032,125420.085,0],[0.232258,128591.5575,0]]])
# ready for choice: profile
yali = get_theValue(working+"/Static_Pressure.txt")
bili = yali / 128591.5575 # yangjian out BC 20211229
FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_bc_type([25,10])
FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static Pressure", [4,[[0.133299,107282.91*bili,0],[0.146126,111072.465*bili,0],[0.158902,114932.9475*bili,0],[0.171526,117628.1925*bili,0],[0.183847,119826.945*bili,0],[0.196164,121833.18*bili,0],[0.20828,123413.85*bili,0],[0.22032,125420.085*bili,0],[0.232258,128591.5575*bili,0]]])

# # ready for choice: constant 
# yali = get_theValue(working+"/Static_Pressure.txt")
# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_bc_type([125,10])
# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Radius", 0.22)
# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static_Pressure", yali)

# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_bc_type([125,10])
# yali = get_theValue(working+"/Static_Pressure.txt")
# # FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static_Pressure", 128591.6)
# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Static_Pressure", yali)
# FT.get_bc_group(FT.get_bc_patch(0, 0, 0)).set_parameter_value("Radius", 0.232258)
# so, it looks like that I have to read the data file by myself rather than useing it.
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_bc_type([113,1])
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Rotational Speed 1", 0)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Rotational Speed 2", zhuansu)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Higher Radius Limit", 1)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Lower Axial Limit", 0.005)
FT.get_bc_group(FT.get_bc_patch(0, 2, 0)).set_parameter_value("Higher Axial Limit", 0.05)
print("MXairfoil: boundary condition setted in numeca")

############################################################################
## set initial solution
############################################################################
FT.get_initial_solution(0).set_mode("turbo")
FT.get_initial_solution(0).set_turbo_patch_pressure("INLET", "Rotor67_flux_1_Main_Blade_upStream_inlet", 90000)
# FT.get_initial_solution(0).set_mode("file")
# FT.get_initial_solution(0).set_restart_filename( mulu+ "/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run")

############################################################################
## set control variables
############################################################################
FT.set_user_solver_precision(1)
FT.set_output_writing_frequency(50)
FT.set_nb_iter_max(700)
print("MXairfoil: control variables setted in numeca")

# add output number
FT.select_azi_output("_VELOCITY_RELATIVE_MACH_NUMBER_")
FT.select_azi_output("_VELOCITY_RELATIVE_W_MAGNITUDE_")
FT.select_azi_output("_VELOCITY_MAGNITUDE_V_")
FT.select_output("_VELOCITY_MAGNITUDE_V_")
FT.select_output("_VELOCITY_RELATIVE_MACH_NUMBER_")

############################################################################
## Run. Save the *.run and call another *.exe 
############################################################################
# FT.save_project_as(saveDir,0)
FT.save_project()
FT.save_selected_computations() #project must saved before save computation, or it will hard to find.

print( "MXairfoil: finish Turbo setting.")

