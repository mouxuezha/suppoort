mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'
working= mulu + '/Turbo_set'
saveDir = mulu + '/testRotor67.iec'
meshDir = mulu + '/testRotor67.igg'
# add output number
FT.select_azi_output("_VELOCITY_RELATIVE_MACH_NUMBER_")
FT.select_azi_output("_VELOCITY_RELATIVE_W_MAGNITUDE_")
FT.select_azi_output("_VELOCITY_MAGNITUDE_V_")
FT.select_output("_VELOCITY_MAGNITUDE_V_")
FT.select_output("_VELOCITY_RELATIVE_MACH_NUMBER_")

FT.get_initial_solution(0).set_mode("file")
FT.get_initial_solution(0).set_restart_filename(mulu+"/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run")
FT.set_MG_flag(0)

FT.set_nb_iter_max(1)

# FT.save_project_as(saveDir,0)
FT.save_project()
FT.save_selected_computations() #project must saved before save computation, or it will hard to find.