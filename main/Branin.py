# Branin function from surrogate modelling book.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
from matplotlib import cm
from matplotlib.ticker import LinearLocator

import time 
import pickle
import os

# save_location = 'C:/Users/y/Desktop/huatu2D.png'
# save_location = 'C:/Users/y/Desktop/DDPGshishi/main/huatu2D.png'
save_location = 'C:/Users/y/Desktop/DDPGshishi/main'

def AckleyFunction(x):
    #implement the function itself
    x = np.array(x)
    x = x.reshape(2,)
    x[0] = x[0] * 32.768*2 - 32.768
    x[1] = x[1] * 32.768*2 - 32.768
    a = 20 
    b = 0.2
    c = 2*np.pi 
    d = x.size
    zhi = -a*np.exp(-b*np.sqrt(1/d*(x**2).sum())) - np.exp(1/d*(np.cos(c*x)).sum()) + a + np.exp(1) 
    zhi = zhi - (21.88100063619471)
    zhi = zhi *(-1)
    zhi = zhi / (21.88100063619471)
    return zhi 

def AckleyFunction2(x):
    chicun = x.shape
    try:
        if chicun[1] != 0 :
            #which means array are inputed. 
            zhi = np.zeros([chicun[0],])
            for i in range(chicun[0]):
                # zhi[i] = BraninFunction([x[i][0],x[i][1]])
                zhi[i] = AckleyFunction([x[i][0],x[i][1]])
    except IndexError  :
        # zhi = BraninFunction(x)
        zhi = AckleyFunction(x)
        zhi = np.array(zhi).reshape(1,)
    return zhi

def BraninFunction(x):
    #implement the function itself
    x = np.array(x)
    pi = np.pi
    x = x.reshape(2,)
    x[0] = x[0] * 15 - 5 
    x[1] = x[1] *15
    zhi = (x[1] - 5.1/4/pi**2*x[1]+5/pi*x[0]-6)**2 + 10 *((1-1/8/pi)*np.cos(x[0])+1) + 5*x[0] 
    zhi = zhi - (-16.457520388653005)
    zhi = zhi / (418.5989847628981- (-16.457520388653005))
    return zhi 

def BraninFunction_normal(x):
    x = np.array(x)
    pi = np.pi
    x = x.reshape(2,)
    x[0] = x[0] * 15 - 5 
    x[1] = x[1] *15
    # zhi = 1/51.5*((x[1] - 5.1/4/pi**2*x[0]**2+5/pi*x[0]-6)**2 + (10-10/8/pi)*np.cos(x[0])-44.81) #this this what paper said 
    zhi = ((x[1] - 5.1/4/pi**2*x[0]**2+5/pi*x[0]-6)**2 + (10-10/8/pi)*np.cos(x[0])-44.81)#this is what pykriging used.
    
    
    ymax = 253.31909601160663
    ymin = -54.40622987907503
    y_normal = (zhi-ymin)/(ymax-ymin)
    return y_normal

def BraninFunction2(x):
    chicun = x.shape
    try:
        if chicun[1] != 0 :
            #which means array are inputed. 
            zhi = np.zeros([chicun[0],])
            for i in range(chicun[0]):
                # zhi[i] = BraninFunction([x[i][0],x[i][1]])
                zhi[i] = BraninFunction_normal([x[i][0],x[i][1]])
    except IndexError  :
        # zhi = BraninFunction(x)
        zhi = BraninFunction_normal(x)
        zhi = np.array(zhi).reshape(1,)
    return zhi 

def ToulanFunction2(x):
    chicun = x.shape
    try:
        if chicun[1] != 0 :
            #which means array are inputed. 
            zhi = np.zeros([chicun[0],])
            for i in range(chicun[0]):
                zhi[i] = ToulanFunction([x[i][0],x[i][1]])
    except IndexError  :
        zhi = ToulanFunction(x)
        zhi = np.array(zhi).reshape(1,)
    return zhi 

def ToulanFunction(x):
    y = [0.3,1]
    x = np.array(x)
    x = x.reshape(2,)
    y = np.array(y)
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

def siweiFunction(x):
    # get a 4 dim function to validate a relatively practical sorrugate model
    x = np.array(x).reshape(1,4)
    y = [0.5,0.5,0.5,0.5]
    y = np.array(y).reshape(1,4)
    jvli = (x-y)**2
    jvli = jvli.sum()

    jiao = np.zeros((16,4))
    jvli_jiao = np.zeros((16,))
    
    for i in range(16):
        if i>0:
            jiao[i] = jiao[i-1]
            jiao[i][3] = jiao[i][3] +1 
        elif i == 0 :
            continue 

        for j in range(4):
            # the most shabi method, traverseing it times and times
            weizhi = 3-j
            if jiao[i][weizhi] ==2:
                jiao[i][weizhi] =0
                jiao[i][weizhi-1] = jiao[i][weizhi-1] + 1 
    
    for i in range(16):
        jvli_jiao_zhongjie = (jiao[i]-y)**2
        jvli_jiao[i] = jvli_jiao_zhongjie.sum()
    jvli_max = np.max(jvli_jiao)
    jvli_norm = jvli/jvli_max
    canshu = 0.15
    zhi = 1 / (jvli_norm + canshu) * canshu
    return zhi 

def siweiFunction2(x):
    # this is for huatu2D 
    chicun = x.shape
    try:
        if chicun[1] != 0 :
            #which means array are inputed. 
            zhi = np.zeros([chicun[0],])
            for i in range(chicun[0]):
                zhi[i] = siweiFunction(x[i])
    except IndexError  :
        zhi = siweiFunction(x)
        zhi = np.array(zhi).reshape(1,)
    return zhi 

def taoke(Function):
    #try another way to form 4D to 2D 
    
    def zhi(x):
        x=np.array(x)
        chicun = x.shape
        x_bu = np.zeros((chicun[0],))
        x = np.array(x)
        # shuru = np.append(x,x_bu+1,axis=1)
        shuru = np.append(x,x_bu+1)
        shuru = np.append(shuru,x_bu+1)
        return Function(shuru)
    return zhi

def taoke_batch(Function):
    def fanhuihanshu(x):
        # this is for huatu2D 
        chicun = x.shape
        try:
            if chicun[1] != 0 :
                #which means array are inputed. 
                zhi = np.zeros([chicun[0],])
                for i in range(chicun[0]):
                    zhi[i] = siweiFunction([x[i][0],x[i][1],0.5,0.5])
        except IndexError  :
            zhi = siweiFunction([x[0],x[1],0.5,0.5])
            zhi = np.array(zhi).reshape(1,)
        return zhi
    return fanhuihanshu

def shishiSin(x):
    x = np.array(x)
    x = x.reshape(2,)
    pi = np.pi
    # jvli = (x**2).sum() # [0,2]
    # jvli = jvli-1 #[0,1]
    jvli = x[0] #[0,1]
    jvli = jvli*2 -1 #[-1,1]
    zhi = np.sin(pi*jvli)
    return zhi 

def shishi2D(x):
    y = x *2
    return y 

def huatu_1():
    print('MXairfoil: test Branin funtion ')
    x1 = np.arange(0,1.01,0.01)
    x2 = np.arange(0,1.01,0.01)
    X1,X2 = np.meshgrid(x1,x2)
    Y = np.zeros(X1.shape)
    for i in range(X1.shape[1]):
        for j in range(X2.shape[0]):
            Y[j][i] = BraninFunction2(np.array([X1[i][i],X2[j][j]]))
    # then plot.
    # Plot the surface.
    norm = cm.colors.Normalize(vmax=Y.max(), vmin=Y.min())
    fig, ax = plt.subplots()
    cset1 = ax.contourf(
    X1, X2, Y, 60,
    norm=norm,alpha=0.7)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    x_label = np.arange(0,1.1,0.1)
    ax.set_xticks(x_label)
    ax.set_yticks(x_label)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('Branin')
    plt.colorbar(cset1)
    plt.savefig('C:/Users/y/Desktop/Branin.png',dpi=300)
    plt.show()

def huatu_2():
    print('MXairfoil: test ToulanFunction funtion ')
    x1 = np.arange(0,1.01,0.01)
    x2 = np.arange(0,1.01,0.01)
    X1,X2 = np.meshgrid(x1,x2)
    Y = np.zeros(X1.shape)
    for i in range(X1.shape[1]):
        for j in range(X2.shape[0]):
            Y[j][i] = ToulanFunction([X1[i][i],X2[j][j]],[0.7,0.3])
    # then plot.
    # Plot the surface.
    norm = cm.colors.Normalize(vmax=Y.max(), vmin=Y.min())
    fig, ax = plt.subplots()
    cset1 = ax.contourf(
    X1, X2, Y, 60,
    norm=norm,alpha=0.7)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    x_label = np.arange(0,1.1,0.1)
    ax.set_xticks(x_label)
    ax.set_yticks(x_label)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('circle')
    plt.colorbar(cset1)
    plt.savefig('C:/Users/y/Desktop/Toulan.png',dpi=300)
    plt.show()

def huatu_3():
    print('MXairfoil: test shishiSin funtion ')
    x1 = np.arange(0,1.01,0.01)
    x2 = np.arange(0,1.01,0.01)
    X1,X2 = np.meshgrid(x1,x2)
    Y = np.zeros(X1.shape)
    for i in range(X1.shape[1]):
        for j in range(X2.shape[0]):
            Y[j][i] = shishiSin([X1[i][i],X2[j][j]])
    # then plot.
    # Plot the surface.
    norm = cm.colors.Normalize(vmax=Y.max(), vmin=Y.min())
    fig, ax = plt.subplots()
    cset1 = ax.contourf(
    X1, X2, Y, 60,
    norm=norm,alpha=0.7)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    x_label = np.arange(0,1.1,0.1)
    ax.set_xticks(x_label)
    ax.set_yticks(x_label)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('circle')
    plt.colorbar(cset1)
    plt.savefig('C:/Users/y/Desktop/shishiSin.png',dpi=300)
    plt.show()

def huatu2D(function):
    print('MXairfoil: test  funtion ')
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
    cset1 = ax.contourf(
    X1, X2, Y, 60,
    norm=norm,alpha=0.7)
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
    plt.show()

def ceshi2D(realf,predictf):
    time_start = time.time()
    N=100 
    X_rand = np.random.uniform(0,1,(N,2))
    # y_real =np.array([])
    # y_predict =np.array([])
    y_real = np.zeros((N,))
    y_predict = np.zeros((N,))

    

    for i in range(N):
        y_real[i] = realf(X_rand[i,:])
        y_predict[i] = predictf(X_rand[i,:])

    SE = (y_real - y_predict)**2
    MSE = np.mean(SE)
    time_end = time.time()
    time_cost =time_end-time_start
    print('MXairfoil:MSE='+str(MSE)+' time_cost ='+str(time_cost))
    return MSE

def ceshiND(realf,predictf,dim):
    #cao ni ma
    time_start = time.time()
    N=100 
    X_rand = np.random.uniform(0,1,(N,dim))
    # y_real =np.array([])
    # y_predict =np.array([])
    y_real = np.zeros((N,))
    y_predict = np.zeros((N,))

    

    for i in range(N):
        y_real[i] = realf(X_rand[i,:])
        y_predict[i] = predictf(X_rand[i,:])

    SE = (y_real - y_predict)**2
    MSE = np.mean(SE)
    time_end = time.time()
    time_cost =time_end-time_start
    print('MXairfoil:MSE='+str(MSE)+' time_cost ='+str(time_cost))
    return MSE



if __name__ =='__main__':
    # huatu2D(AckleyFunction2)
    # print('huatu2D(AckleyFunction2)')
    flag = 2 
    if flag == 0:
        zhi = siweiFunction([1,1,1,1])
        zhi2 = taoke(siweiFunction)([1,1])
        huatu2D(taoke_batch(taoke(siweiFunction)))
        print('MXairfoil: huatu2D(siweiFunction2)')
    elif flag ==1:
        huatu2D(taoke_batch(BraninFunction_normal))
    elif flag ==2:
        huatu2D(ToulanFunction2)

    print('MXairfoil: finish a test process for test function. En Taro XXH!')