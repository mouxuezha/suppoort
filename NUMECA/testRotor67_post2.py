CFViewBackward(1210,)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'
mulu_jieguo = mulu + '/main/jieguo'
# this is for huatuing in r percent.

# load case in 3D
FileOpenProject(mulu+'/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run',)
MacroModuleLoad('TW',)

QntFieldDerived(0 ,'V' ,'sqrt(Vxyz_X*Vxyz_X + Vxyz_Y*Vxyz_Y  + Vxyz_Z*Vxyz_Z)' ,'' ,'0')


CutPlaneSave(0.5,0,0,1,0,0,2,0)
ViewPlaneX()
SetCamera(-0.415654,0.0325705,0.0516539,0.172498,0.0325705,0.0516539,0,1,0,0.235261,0.118142)
GmtToggleBoundary()
# SelectedSurfacesAdd('Rotor67_hub_(r.p.m. -16043)')
# SelectedSurfacesAdd('Rotor67_shroud')
# SelectedSurfacesAdd('Rotor67_blade_(r.p.m. -16043)')
SelectedSurfacesRemove('Rotor67_hub_(r.p.m. -16043)')
SelectedSurfacesRemove('Rotor67_shroud')
SelectedSurfacesRemove('Rotor67_blade_(r.p.m. -16043)')
# GmtToggleBoundary()

def plot_total_pressure(bili):
# then plot total pressure.
	p_min = 60000
	p_max = 200000
	if bili>0.95:
		p_max = 330000
	QntFieldScalar('Absolute Total Pressure')
	SclContourSmooth()
	RprRangeActiveSurfaces()
	SclIsolineMulti(2,4,p_min,p_max,5000,1)
	RprRangeIn(p_min,p_max)
	ColormapNumOfSmallTicks(5)
	ColormapNumbersFormat(0,1,3)
	ColormapTicksNumberDistance(0.0405)
	ColormapNumOfSmallTicks(3)
	SetNumecaLogo(0,0)
	ColormapTicksNumberTextType(0,24,2,0,1,0,0,1,0,0,0,0)
	ColormapLabelTextType(0,26,2,2,1,0,0,1,0,0,0,0)
	mulu_total_pressure = mulu_jieguo + '/contour_total_pressure'+str(bili)+'.png'
	Print(8,0,1,1,100,5000,3000,0 ,mulu_total_pressure,'',1,1,1)

plot_total_pressure(0.5)

# CutPlaneSave(0.1,0,0,1,0,0,2,0)
# GmtToggleBoundary()
# SelectedSurfacesRemove('CUT1')
# GmtToggleBoundary()
# DeleteAll()
# plot_total_pressure(0.1)

# bili_list = [0.1,0.3,0.7,0.99]
bili_list = [0.1,0.99]
for i in range(len(bili_list)):
    bili_i = bili_list[i]
    surface_name = 'CUT'+str(i+1)
    CutPlaneSave(bili_i,0,0,1,0,0,2,0)
    # GmtToggleBoundary()
    SelectedSurfacesRemove(surface_name)
    GmtToggleBoundary()
    DeleteAll()
    plot_total_pressure(bili_i)
    if i == len(bili_list)-1:
        surface_name = 'CUT'+str(i+2)
        SelectedSurfacesRemove(surface_name)

# then plot V
def plot_V(bili):
# then plot total pressure.
	V_min = 0
	V_max = 400
	if bili>0.95:
		V_max = 600
	QntFieldScalar('V')
	SclContourSmooth()
	RprRangeActiveSurfaces()
	SclIsolineMulti(2,4,V_min,V_max,25,1)
	RprRangeIn(V_min,V_max)
	ColormapNumbersFormat(0,0,3)
	SetNumecaLogo(0,0)
	ColormapTicksNumberTextType(0,24,2,0,1,0,0,1,0,0,0,0)
	ColormapLabelTextType(0,26,2,2,1,0,0,1,0,0,0,0)
	mulu_total_pressure = mulu_jieguo + '/contour_V'+str(bili)+'.png'
	Print(8,0,1,1,100,5000,3000,0 ,mulu_total_pressure,'',1,1,1)

DeleteAll()
bili_list.insert(0,0.5)
for i in range(len(bili_list)):
    bili_i = bili_list[i]
    surface_name = 'CUT'+str(i+1)
    SelectedSurfacesAdd(surface_name)
    plot_V(bili_i)
    SelectedSurfacesRemove(surface_name)
    DeleteAll()