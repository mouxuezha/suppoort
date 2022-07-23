CFViewBackward(1210,) 
mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor37'
#post process in CFviewer

CFViewBackward(1210)
FileOpenProject(mulu+ '/testRotor37/testRotor37_computation_1/testRotor37_computation_1.run')
MacroModuleLoad('TW')

QntFieldVector('Wxyz')


SelectedSurfacesRemove('row 1_hub_(r.p.m. -17188)')
SelectedSurfacesRemove('row 1_blade_(r.p.m. -17188)')
GmtToggleBoundary()
SelectedSurfacesRemove('row 1_shroud')

# SelectedSurfacesAdd('row 1_blade_(r.p.m. -17188)')
# SelectedSurfacesRemove('row 1_blade_(r.p.m. -17188)')
SelectedSurfacesAdd('row_1_flux_1_Main_Blade_skin.Imin blade_(aap-ss)_rotating')
RenderHidden()
StreamLineRepresentation(0,0 ,'Static Temperature',1,0,1,0,0,0,1,1,8)
StreamLineAdvancedParameters(1,0,0,0.01,1,3,1,5)
StreamLineComputationParameters(200,20,4,1,0,5 ,'Wxyz')
StreamLineCurveType(0,1,1,0,0,0,1,1,0,0,0,0,0.2,5,1,0)
StreamLineSurfaceType(0,1,1,0,0,1,4,0,0,0,1,0 ,'metal - polished',1)
StreamLineArrowParameters(1,1,17.7589)

SetCamera(0.360087,0.31463,-0.368472,0.218273,0.0211463,0.00284084,0.957829,-0.166966,0.233852,0.197633,0.103953)