mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'

# -*- coding: utf-8 -*-
##################################################################################
## 
## Numeca Int. sa - AutoGrid5 Python script
##
## The aim of this script is the attempt of the main features of AutoGrid5
## Trying to build a mesh from *.geomTurbo file which generated by my own
## matlab code
##
##
## Author: 		mouxuezha
## Created on:		9 December 2021
## En Taro XXH! 
## 
##################################################################################
##
## USER INPUT
## Adapt the mulu to a suitable directory and execute the script in AutoGrid5
##

print "MXairfoil: Autogrid process started, En Taro XXH!"

a5_init_new_project_from_a_geomTurbo_file(mulu + "/Rotor67.geomTurbo")
a5_set_configuration_units("Centimeters") 
row(1).set_name("Rotor67")

a5_treetclUpdate()


###################################################################################
## PART 4: Configuring rotor using yangjian mode
###################################################################################

row(1).blade(1).set_geometry_data_reduction_distance_criteria(1e-6)

row(1).blade(1).set_geometry_data_reduction(1)

row(1).blade(1).check_geometry()

row(1).blade(1).apply_data_reduction() 

row(1).row_wizard().initialize(6,1,-16043,22)

# row(1).row_wizard().hub_fillet_is_asked(1)
# row(1).blade(1).fillet(1).set_radius_at_leading_edge(0.178)
# row(1).blade(1).fillet(1).set_radius_at_trailing_edge(0.178)

row(1).row_wizard().tip_gap_is_asked(1)
row(1).row_wizard().set_tip_gap_width_at_leading_edge(0.1)
row(1).row_wizard().set_tip_gap_width_at_trailing_edge(0.1)

row(1).row_wizard().set_flow_path_number(73) # corresponding to the spanwise grid point number

row(1).row_wizard().set_row_cell_width_at_wall(0.0001)

row(1).row_wizard().set_grid_level(-4)

row(1).row_wizard().generate() # To apply all the settings set in the row_wizard class 

###################################################################################
## PART 5: Generate 3D mesh and save template
###################################################################################
# select all rows and compute 3D mesh
select_all()
a5_start_3d_generation()

# save the project
a5_save_project(mulu+"/testRotor67.trb")

# os._exit(0)
# good, it is useful. these yangjian things are very convenient to use.

print "MXairfoil: Autogrid finished, En Taro XXH!"