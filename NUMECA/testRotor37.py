mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor37'

print "MXairfoil: Autogrid process started, En Taro XXH!"

a5_init_new_project_from_a_geomTurbo_file(mulu + "/Rotor37shishi.geomTurbo")
a5_set_configuration_units("Centimeters") 
row(1).set_name("row 1")

a5_treetclUpdate()

row(1).blade(1).set_geometry_data_reduction_distance_criteria(1e-6)

row(1).blade(1).set_geometry_data_reduction(1)

row(1).blade(1).check_geometry()

row(1).blade(1).apply_data_reduction() 

row(1).row_wizard().initialize(6,1,-17188,36)

row(1).row_wizard().tip_gap_is_asked(1)

row(1).row_wizard().set_tip_gap_width_at_leading_edge(0.0356)

row(1).row_wizard().set_tip_gap_width_at_trailing_edge(0.0356)

row(1).row_wizard().set_flow_path_number(73) # corresponding to the spanwise grid point number

row(1).row_wizard().set_row_cell_width_at_wall(0.0003)

row(1).row_wizard().set_grid_level(-2) #-2 for 129W, -7 for 62W,

row(1).row_wizard().generate() # To apply all the settings set in the row_wizard class 

select_all()
a5_start_3d_generation()

a5_save_project(mulu+"/Rotor37shishi.trb")

# os._exit(0)
# good, it is useful. these yangjian things are very convenient to use.

print "MXairfoil: Autogrid finished, En Taro XXH!"