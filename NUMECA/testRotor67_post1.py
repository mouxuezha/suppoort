CFViewBackward(1210,)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'
#post process in CFviewer
# FileOpenProject(mulu+'/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run',)
# MacroModuleLoad('TW',)

FileOpenProject(mulu + '/testRotor67/testRotor67_computation_1/testRotor67_computation_1.me.cfv')
MacroModuleLoad('TW')

# QntFieldDerived(0 ,'V' ,'sqrt(Vxyz_X*Vxyz_X + Vxyz_Y*Vxyz_Y  + Vxyz_Z*Vxyz_Z)' ,'' ,'0')

SetCamera(0.0540192,0.176915,0.83298,0.0540192,0.176915,0,0,1,0,0.333192,0.105452)
SelectedSurfacesRemove('domain4')
SelectedSurfacesRemove('domain5')

# =============================================================================
DeleteAll()
mulu_static_pressure = mulu + '/main/jieguo/contour_static_pressure.png'
# huatu for static pressure.
QntFieldScalar('Absolute Total Pressure')
SclContourSmooth()
RprRangeActiveSurfaces()
SclIsolineMulti(2,4,70000,170000,7142.85714286,1)
# switch off 'NUMECA'
SetNumecaLogo(0,0)
# set front type
ColormapNumOfSmallTicks(3)
ColormapTicksNumberTextType(0,24,2,0,1,0,0,1,0,0,0,0)
ColormapLabelTextType(0,26,2,2,1,0,0,1,0,0,0,0)
Print(8,0,1,1,100,5000,3000,0 ,mulu_static_pressure,'',1,1,1)

# =============================================================================
DeleteAll()
mulu_relative_Ma = mulu + '/main/jieguo/contour_relative_Ma.png'
# huatu for relative Ma 
# try:
	# QntFieldScalar('Relative Mach Number')
# except:
    # QntFieldDerived(0 ,'shengsu' ,'sqrt(1.4*287.06*Static Temperature)' ,'' ,'0')
	# QntFieldDerived(0 ,'Ma' ,'sqrt(Vxyz_Y*Vxyz_Y + Vxyz_X*Vxyz_X  + Vxyz_Z*Vxyz_Z )/shengsu' ,'' ,'0')
try:
    QntFieldScalar('Relative Mach Number')
    SclContourSmooth()
    SclIsolineMulti(2,4,0.4,1.2,0.0571429,1)
    ColormapNumOfSmallTicks(3)
    ColormapTicksNumberTextType(0,24,2,0,1,0,0,1,0,0,0,0)
    ColormapLabelTextType(0,26,2,2,1,0,0,1,0,0,0,0)
    Print(8,0,1,1,100,5000,3000,0 ,mulu_relative_Ma,'',1,1,1)
except:
    print('MXairfoil: fail to get mulu_relative_Ma')
