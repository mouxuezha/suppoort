CFViewBackward(1210,)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'

FileOpenProject(mulu+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run',)
MacroModuleLoad('TW',)
CutPlaneSaveFrom3Points(0, 0, 0, 0, 0.00773624, 0, 0.12, 0.12, 0)
QntFieldScalar('Static Pressure',)
SclContourSmooth()
ViewScroll(0, 0, 0)
MacroModuleLoad('TW')

QntFieldDerived(0 ,'V' ,'sqrt(Vxyz_X*Vxyz_X + Vxyz_Y*Vxyz_Y  + Vxyz_Z*Vxyz_Z)' ,'' ,'0')
QntFieldDerived(0 ,'Vx' ,'sqrt(Vxyz_X*Vxyz_X)' ,'' ,'0')

QntFieldDerived(0, 'Cpt', '(Total Pressure-101325)/101325', '', '0')
QntFieldDerived(0, 'Cpt2', '(Total Pressure-101325)/101325/0.1273', '', '0')
QntFieldDerived(0 ,'jiaodu' ,'atan(Vxyz_Y/Vxyz_X)/pi*180' ,'' ,'0')


# QntFieldScalar('Cpt',)
# SclContourSmooth()
# SclPlotBoundarySolid(0)

SelectedSurfacesRemove('Block_1.Imin Solid')
SelectedSurfacesRemove('Block_1.Imax Solid')
SelectedSurfacesRemove('CUT1')
SelectedSurfacesAdd('Block_1.Jmin Inlet')
QntFieldScalar('Total Pressure')
Ptinlet=SclAverage()
# print('============================================')
# print('MXairfoil: Ptinlet =')
# print(Ptinlet)
# print('============================================')
wenjianming = mulu+'/testCDA1/jieguo/'
Ptinlet_file = open(wenjianming+'Ptinlet.dat','w')
Ptinlet_file.write(str(Ptinlet)) 
Ptinlet_file.close()


# moew post process
# SelectedSurfacesAdd('Block_1.Jmax Outlet')
# QntFieldScalar('Density')
# rhom = SclAverage()
# QntFieldScalar('V')
# Vm = SclAverage()
QntFieldScalar('Total Pressure')
# Ptin = SclAverage()
Ptin = WeightedIntegral()
Ptin_file = open(wenjianming+'Ptin.dat','w')
Ptin_file.write(str(Ptin)) 
Ptin_file.close()

QntFieldScalar('Static Pressure')
#Psin = SclAverage()
Psin = WeightedIntegral()
Psin_file = open(wenjianming+'Psin.dat','w')
Psin_file.write(str(Psin)) 
Psin_file.close()

SelectedSurfacesRemove('Block_1.Jmin Inlet')
SelectedSurfacesAdd('Block_1.Jmax Outlet')
QntFieldScalar('Total Pressure')
# Ptout = SclAverage()
Ptout = WeightedIntegral()
Ptout_file = open(wenjianming+'Ptout.dat','w')
Ptout_file.write(str(Ptout)) 
Ptout_file.close()

QntFieldScalar('Static Pressure')
# Psout = SclAverage()
Psout = WeightedIntegral()
Psout_file = open(wenjianming+'Psout.dat','w')
Psout_file.write(str(Psout)) 
Psout_file.close()

omega = (Ptin - Ptout)/(Ptin - Psin)
omega_file = open(wenjianming+'omega.dat','w')
omega_file.write(str(omega)) 
omega_file.close()

sigma = Ptout / Ptin 
sigma_file = open(wenjianming+'sigma.dat','w')
sigma_file.write(str(sigma)) 
sigma_file.close()

rise = Ptin/Psin
rise_file = open(wenjianming+'rise.dat','w')
rise_file.write(str(rise)) 
rise_file.close()

QntFieldDerived(0, 'Cps', '(Static Pressure-'+str(Psin)+')/('+str(Ptin)+'-'+str(Psin)+')', '', '0')
# QntFieldDerived(0, 'Cps2', '(Static Pressure-99318.5)/(104650-99318.5)', '', '0')
SelectedSurfacesRemove('Block_1.Jmin Inlet')
SelectedSurfacesRemove('Block_1.Jmax Outlet')
SelectedSurfacesAdd('Block_1.Imin Solid')
SelectedSurfacesAdd('Block_1.Imax Solid')
QntFieldScalar('Cps',)
SclContourSmooth()
SclPlotBoundarySolid(0)
PlotCurveOutput(wenjianming+'Cps.dat')

def get_theValue(working):
    # legacy code, get the value from configure file. It is not very ingenious.
    rotational_speed = open(working,'r')
    strBuffer= rotational_speed.read()
    value=float(strBuffer) 
    # value=int(strBuffer) 
    print('MXairfoil: get the value  '+strBuffer)
    print('in the dictionary: '+ working)
    return value 

# establish a figure.
ViewPlaneZ()
ViewPlaneZ()
ViewZoomAll(1)
ViewZoomAreaIn(-0.411345,0.401889,-0.643175,1.08823)
SetNumecaLogo(0,0)
ColormapLabelTextType(0,26,2,2,1,0,0,1,0,0,0,0)
ColormapNumOfSmallTicks(3)
ColormapTicksNumberTextType(0,30,2,0,1,0,0,1,0,0,0,0)
ColormapLabelTextType(10,32,2,2,1,0,0,1,0,0,0,0)

N_step = int(get_theValue(mulu+'/N_step.txt'))
mulu_fig_Pt = mulu+'/output/contour-Pt/Pt'+str(N_step) +'.tif'
mulu_fig_V = mulu+'/output/contour-V/V'+str(N_step) +'.tif'
mulu_fig_Ps = mulu+'/output/contour-Ps/Ps'+str(N_step) +'.tif'

# # plot the color map of V 
SelectedSurfacesAdd('Block_1.Imax Solid')
SelectedSurfacesAdd('Block_1.Imin Solid')
QntFieldScalar('V')
SclContourSmooth()
Print(6,0,0,1,100,1701,913,0 ,mulu_fig_V,'V',1,1,1)

# # plot the color map of Static pressure.
SelectedSurfacesRemove('Block_1.Imax Solid')
SelectedSurfacesRemove('Block_1.Imin Solid')
QntFieldScalar('Static Pressure')
RprRangeIn(93000,103300)
SclContourSmooth()
Print(6,0,0,1,100,1701,913,0 ,mulu_fig_Ps,'Ps',1,1,1)

# plot the color map of Total Pressure
QntFieldScalar('Total Pressure')
RprRangeIn(93000,108000)
SclContourSmooth()
Print(6,0,0,1,100,1701,913,0 ,mulu_fig_Pt,'Pt',1,1,1)

Quit()