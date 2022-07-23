from distutils.log import error
from re import X
from turtle import shape
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
from matplotlib import cm
from matplotlib.ticker import LinearLocator

import time 
import pickle
import os

# demo functions for further use. updated from 'Branin.py'
class DemoFunctions(object):
    def __init__(self):
        self.save_location = 'C:/Users/y/Desktop/DDPGshishi/main'
        self.point_max = np.array([0.3,1])

    def ToulanFunction2(self,x):
        chicun = x.shape
        try:
            if chicun[1] != 0 :
                #which means array are inputed. 
                zhi = np.zeros([chicun[0],])
                for i in range(chicun[0]):
                    zhi[i] = self.ToulanFunction([x[i][0],x[i][1]])
        except IndexError  :
            zhi = self.ToulanFunction(x)
            zhi = np.array(zhi).reshape(1,)
        return zhi 

    def ToulanFunction(self,x):
        y = self.point_max
        x = np.array(x)
        x = x.reshape(2,)
        jvli = (x-y)**2
        # zhi = 1-jvli.sum()*2
        jvli1 = ([0,0]-y)**2
        jvli2 = ([0,1]-y)**2
        jvli3 = ([1,0]-y)**2
        jvli4 = ([1,1]-y)**2
        jvli_max = np.max([jvli1.sum(),jvli2.sum(),jvli3.sum(),jvli4.sum()])
        jvli_norm = jvli.sum()/jvli_max
        canshu = 0.15
        zhi = 1 / (jvli_norm + canshu) * canshu
        return zhi  

    def huatu2D(self):
        print('MXairfoil: test  funtion ')
        save_location = self.save_location
        function = self.ToulanFunction2

        x1 = np.arange(0,1.01,0.01)
        x2 = np.arange(0,1.01,0.01)
        X1,X2 = np.meshgrid(x1,x2)
        Y = np.zeros(X1.shape)
        for i in range(X1.shape[1]):
            for j in range(X2.shape[0]):
                Y[j][i] = function(np.array([X1[i][i],X2[j][j]]))

        wenjianing_X1 = save_location + '/visual2DX1.pkl'
        wenjianing_X2 = save_location + '/visual2DX2.pkl'
        wenjianing_Y1 = save_location + '/visual2DY1.pkl'
        wenjianing_Y2 = save_location + '/visual2DY2.pkl'

        pickle.dump(X1,open(wenjianing_X1,'wb'))
        pickle.dump(X2,open(wenjianing_X2,'wb'))
        if os.path.exists(wenjianing_Y1):
            pickle.dump(Y,open(wenjianing_Y2,'wb'))
        else:
            pickle.dump(Y,open(wenjianing_Y1,'wb'))
        # then plot.
        # Plot the surface.
        norm = cm.colors.Normalize(vmax=Y.max(), vmin=Y.min())
        fig, ax = plt.subplots()
        cset1 = ax.contourf(X1, X2, Y, 60,norm=norm,alpha=0.7)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        x_label = np.arange(0,1.1,0.1)
        ax.set_xticks(x_label)
        ax.set_yticks(x_label)
        ax.set_xlabel('X1')
        ax.set_ylabel('X2')
        ax.set_title('Test Function')
        plt.colorbar(cset1)
        plt.savefig(save_location+'/huatu2D.png',dpi=300)
        # plt.show()

    def set_point_max(self,X_m):
        self.point_max = X_m 
        chicun = X_m.shape
        self.x_dim = chicun[0]
        X_far = np.zeros(chicun[0])
        for i in range(chicun[0]):
            if X_m[i]>0.5:
                X_far[i] = 1 
            else:
                X_far[i] = 0 
        self.jvli_max = (X_far-X_m)**2
        self.jvli_max = self.jvli_max.sum() 

    def ToulanFunction_general(self,x):
        # this is for 3D case, there are 18 design variable, so a ToulanFunction with len(x) = 18 is needed.
        chicun = x.shape
        if chicun[0] != self.x_dim:
            raise Exception('MXairfoil: unmatch x_dim in demo fucktion, G.')
        # # first establish corners
        # corners = np.zeros([2**18,18])
        # for i in range(2**18):
        #     index_10 = i 
        #     # transfer from decimalism to binary
        #     for j in range(18):
        #         weishu = 2 
        #         this_bit = index_10 % weishu
        #         index_10 = (index_10 - this_bit)//2
        #         corners[i][17-j] = this_bit
        #         if index_10 == 0:
        #             break
        # # too big time consumption
        
        # an another silu is used, more tactful.
        
        # then calculate jvlis
        jvli= (x-self.point_max)**2 
        jvli_norm = jvli.sum()/self.jvli_max
        canshu = 0.15
        zhi = 1 / (jvli_norm + canshu) * canshu
        return zhi          


        

if __name__ == '__main__':
    # weizhi = r'C:\Users\y\Desktop\DDPGshishi\agents\jieguo_DDPG_master6'
    # shishi = DemoFunctions()
    # shishi.save_location = weizhi
    # shishi.point_max = np.array([0.3,0.7])
    # shishi.huatu2D()

    weizhi = r'C:\Users\y\Desktop\DDPGshishi\demo_shishi'
    shishi = DemoFunctions()
    shishi.save_location = weizhi
    dian = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
    dian2 = np.zeros(18)
    shishi.set_point_max(dian)
    shishi.ToulanFunction_general(dian2)
