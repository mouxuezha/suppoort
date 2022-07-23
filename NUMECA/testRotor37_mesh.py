CFViewBackward(1210)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor37'

FileOpenProject(mulu+'/testRotor37/testRotor37_computation_1/testRotor37_computation_1.run')
MacroModuleLoad('TW')

SelectedSurfacesRemove('row 1_shroud')
DefaultSectionCurveType(0,0,0,0,0,0,1,2,0,0,0,0,0.4,5,1,1)
SelectedSurfacesAdd('row 1_shroud')
GmtToggleBoundary()
SelectedSurfacesRemove('row 1_shroud')
RenderGouraud()
GmtToggleGrid()
RenderHidden()

mulu_fig_da = mulu+'/main/'+'mesh_all.tif'
mulu_fig_qian = mulu+'/main/'+'mesh_in.tif'
mulu_fig_hou = mulu+'/main/'+'mesh_out.tif'
SetNumecaLogo(0,0)

SetCamera(0.518384,0.218248,-0.541668,0.193888,-0.000302168,-0.00985327,0.861029,-0.323432,0.392455,0.264088,0.130058)
# Print(6,0,1,1,100,4096,2160,0 ,mulu_fig_da ,'',1,1,1)
Print(6,0,1,1,100,1920,1080,0 ,mulu_fig_da ,'',1,1,1)

SetCamera(0.193124,-0.00971784,-0.0264258,0.188279,-0.0129807,-0.0184861,0.861029,-0.323432,0.392455,0.00161493,0.000795324)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_qian ,'',1,1,1)

SetCamera(0.254679,0.0737008,0.0581462,0.242126,0.062684,0.0553472,0.668031,-0.738991,-0.0873345,0.00221967,0.00109315)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_hou ,'',1,1,1)

SetCamera(0.518384,0.218248,-0.541668,0.193888,-0.000302168,-0.00985327,0.861029,-0.323432,0.392455,0.264088,0.130058)