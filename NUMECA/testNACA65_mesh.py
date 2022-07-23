CFViewBackward(1210,)
mulu = 'C:/Users/y/Desktop/EnglishMulu/testNACA65'

OpenCGNSAutogrid(mulu+'/testNACA65.cgns')
GmtToggleGrid()

mulu_fig_da = mulu+'/output/'+'mesh_all.tif'
mulu_fig_qian = mulu+'/output/'+'mesh_in.tif'
mulu_fig_hou = mulu+'/output/'+'mesh_out.tif'
SetNumecaLogo(0,0)

ViewPlaneX()
ViewPlaneY()
ViewPlaneZ()
ViewPlaneZ()

SetCamera(3.80662,10.1985,11.5056,3.80662,10.1985,0.5,0,1,0,4.40225,26.004)
Print(6,0,1,1,100,1920,1080,0 ,mulu_fig_da ,'',1,1,1)
# SetCamera(0.204443,12.407,1.2563,0.204443,12.407,0.5,0,1,0,0.232336,1.3724)
SetCamera(-0.398655,-0.131721,0.898647,-0.398655,-0.131721,0.5,0,1,0,0.159459,0.941922)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_qian ,'',1,1,1)
SetCamera(10.2605,20.2729,1.60918,10.2605,20.2729,0.5,0,1,0,0.128625,0.75979)
Print(6,0,1,1,100,1080,720,0 ,mulu_fig_hou ,'',1,1,1)
SetCamera(5.23497,5.01678,8.48518,5.23497,5.01678,0.5,0,1,0,3.19407,18.8673)