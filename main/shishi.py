'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))  # first derivative # woc, haiyou zhezhong wanfa? got it 

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[1].add_collection(lc)
fig.colorbar(line, ax=axs[1])

axs[0].set_xlim(x.min(), x.max())
axs[0].set_ylim(-1.1, 1.1)
plt.savefig('shishi.png',dpi=700)
plt.show()

'''

'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)


# Plot
# ax = plt.figure().add_subplot(projection='3d')
fig = plt.figure()
ax = Axes3D(fig)
ax = plt.axes(projection='3d')


ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.savefig('shishi.png',dpi=700)
plt.show()


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

# ax = plt.figure().add_subplot(projection='3d')

fig= plt.figure()
ax = plt.axes(projection='3d')

X, Y, Z = axes3d.get_test_data(0.05)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

from transfer import transfer
from parameters import parameters # can not extend enum class
from DemoFunctions import DemoFunctions

class shishi_inheritance(transfer,DemoFunctions):
    def __init__(self,dim):
        super(shishi_inheritance, self).__init__(dim=dim)
        # super(DemoFunctions, self).__init__() # shishi_inheritance.__init__ has been overwrited, so __init__ of father classes have to be called explicitly. # but it seems nothing would happen if I dont call that.
        pass

if __name__ =='__main__':
    shishi = shishi_inheritance(114514)
    pass
'''
'''
from huatu import huatu
import numpy as np

data_raw_reward = np.array([[10,0.79570652],[699,0.79575564],[749,0.79806651],[849,0.80012143]])


data_ave_state = np.array([10.98251244056205,39.910314856927485,15.125802373752245,36.88753384278077,60.25070891690336,59.678387670585565,59.93445714372223,63.39584573088648,66.18343714454835,63.09490895772683,68.80634623259104,71.03661184581053,66.66763920784797,67.35073478351029,71.15335928172371,70.87576538353811,72.40348380917325])
N=len(data_ave_state)
episode = np.zeros((N,))
for i in range(N):
    episode[i] = i*50+49

data_ave_state = np.append(episode.reshape(N,1),data_ave_state.reshape(N,1),axis=1)

weizhi =r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\二维的\2021年9月7日改了相应维度之后不带限制的\agent0_2dim0.0031137096088899694'
# tu=huatu(input = data_ave_state)
# tu.set_location(weizhi)
# tu.huatu2D('episode','average reward','Reward-Episode relation')
# tu.save_all()

tu=huatu(input = data_raw_reward)
tu.set_location(weizhi)
tu.huatu2D('episode','Optimization reward','Optimization-Episode relation')
tu.save_all()
'''
import time
import numpy as np

class record_progress:
    def __init__(self,**kargs) :
        self.N_points = kargs['N_points']
        self.N_calculated = 0 
        self.flag_Xgenerate = 0
        self.flag_Ktrain = 0 
        self.flag_Datacheck = 0         
        pass
    def check_progress(self):
        # this is to check the process while running.
        rizhi = 'MXairfoil: check the process... \n    generating X:' + str(self.flag_Xgenerate) + '\n    calculating CFD: ' + str(round(100.0*self.N_calculated/self.N_points,2)) + '% \n    data checking: ' + str(self.flag_Datacheck)+ '\n    generating kriging model:'+ str(self.flag_Xgenerate)
        print(rizhi)
        return rizhi
        # if 'self.flag_Xgenerate' in vars():
        # if hasattr(self,'flag_Xgenerate'):
        #     rizhi = 'MXairfoil: check the process... \n    generating X:' + str(self.flag_Xgenerate) + '\n    calculating CFD: ' + str(100.0*self.N_calculated/self.N_points) + '% \n    generating kriging model:'+ str(self.flag_Xgenerate)
        #     print(rizhi)
        #     # if calling it every calculating
        #     self.N_calculated = self.N_calculated+1
        # else:
        #     # which means calling it for the first time.
        #     self.N_calculated = 0 
        #     self.flag_Xgenerate = 0
        #     self.flag_Ktrain = 0 
        #     self.flag_datacheck = 0 
    def calculate_1ci(self):
        self.N_calculated = self.N_calculated + 1 
    def Xgenerate_done(self):
        self.flag_Xgenerate = 1
    def Krigingtrain_done(self):
        self.flag_Ktrain = 1
    def Detacheck_done(self):
        self.flag_Datacheck = 1         
    def paoyixia(self):
        while(1):
            time.sleep(1)
            self.check_progress()
            self.N_calculated = self.N_calculated +1 

if __name__ =='__main__':
    # shishi1 = record_progress(N_points=1234)
    # shishi1.paoyixia()
    # x_test = np.array([0.5,0.6,0.4,0.5])
    # x_all = np.array([x_test,x_test])
    # x_all2 = np.array([x_test])
    # for i in range(5):
    #     x_all2 = np.append(x_all2,x_test.reshape(1,4),axis=0)
    # shishi = np.var(x_test)
    shishi = round(np.random.uniform(0,1)*100)
    print(shishi)
    pass
 

