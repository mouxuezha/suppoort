import numpy as np 
import copy

class transfer():
    # define a unity transfer, to clear up the code and make it more yangjian
    def __init__(self,**kargs):
        # defaut value:
        self.real_obs_space_h = np.array([0.35,-0.22,0.55,8])
        self.real_obs_space_l = np.array([0.25,-0.38,0.35,5])
        self.normal_obs_space_h =np.array([1,1,1,1])
        self.normal_obs_space_l =np.array([-1,-1,-1,-1]) 
        self.dx = 0.1
        self.surrogate_obs_space_h = np.array([1+self.dx,1+self.dx,1+self.dx,1+self.dx])
        self.surrogate_obs_space_l = np.array([0-self.dx,0-self.dx,0-self.dx,0-self.dx])

        self.dim = 4 
        self.tishi = 0 

        # these lines are trying to do something related to constraints.
        # original point in surrogate model: [0.0558,1.0513,35.8]
        # do not look for trouble, real_con_space should be relatively narrow. 
        self.dim_constraints = 2 
        
        self.real_con_space_h = np.array([1.0515,38.0])
        self.real_con_space_l = np.array([1.0509,34.0])
        self.normal_con_space_h = np.array([1.0,1.0])
        self.normal_con_space_l = np.array([-1.0,-1.0])

        if 'dx' in kargs:
            self.dx = kargs['dx']
        if 'dim' in kargs:
            self.dim = kargs['dim']
        if 'real_obs_space_h' in kargs:
            self.real_obs_space_h = kargs['real_obs_space_h']
        if 'real_obs_space_l' in kargs:
            self.real_obs_space_l = kargs['real_obs_space_l']
        if 'normal_obs_space_h' in kargs:
            self.normal_obs_space_h = kargs['normal_obs_space_h']
        else:
            self.normal_obs_space_h = np.ones(self.dim)
        if 'normal_obs_space_l' in kargs:
            self.normal_obs_space_l = kargs['normal_obs_space_l']
        else:
            self.normal_obs_space_l = np.ones([1,self.dim])*(-1)

        if 'surrogate_obs_space_h' in kargs:
            self.surrogate_obs_space_h = kargs['surrogate_obs_space_h']
        else:
            self.surrogate_obs_space_h = np.ones([1,self.dim])+self.dx
        if 'surrogate_obs_space_l' in kargs:
            self.surrogate_obs_space_l = kargs['surrogate_obs_space_l']
        else:
            self.surrogate_obs_space_l = np.zeros([1,self.dim])-self.dx
        if 'tishi' in kargs:
            self.tishi = kargs['tishi']
        if 'dim_constraints' in kargs:
            self.dim_constraints = kargs['dim_constraints']
        if 'real_con_space_h' in kargs:
            self.real_con_space_h = kargs['real_con_space_h']    
        if 'real_con_space_l' in kargs:
            self.real_con_space_l = kargs['real_con_space_l']   
        if 'normal_con_space_h' in kargs:
            self.normal_con_space_h = kargs['normal_con_space_h']
        if 'normal_con_space_l' in kargs:
            self.normal_con_space_l = kargs['normal_con_space_l']              
        
        # then check the transfer
        chicun = self.real_obs_space_h.shape
        chicun2 = self.normal_obs_space_h.shape
        if (chicun[0] != chicun2[0])or(chicun[0] != self.dim)or(chicun2[0] != self.dim):
            raise Exception('MXairfoil: dimension of obs space mismatching')
        
    def real_to_surrogate(self,state_real):
        # from real to [0-dx,1+dx], then from [0-dx,1+dx] to [-1,1]
        # dx = 0.0
        state_real2,chicun = self.duiqi(state_real)
        real_obs_space_h=self.real_obs_space_h[0:self.dim]
        real_obs_space_l=self.real_obs_space_l[0:self.dim]
        # this is where the differents is
        surrogate_obs_space_h = self.surrogate_obs_space_h[0:self.dim] - self.dx
        surrogate_obs_space_l = self.surrogate_obs_space_l[0:self.dim] + self.dx

        real_state_bili = (real_obs_space_h-real_obs_space_l)/(surrogate_obs_space_h - surrogate_obs_space_l)
        real_state_c = (real_obs_space_h + real_obs_space_l)/2
        surrogate_state_c = ( surrogate_obs_space_h + surrogate_obs_space_l ) /2
    
        surrogate_state = (state_real2 - real_state_c) / real_state_bili + surrogate_state_c 

        if self.tishi > 0:
            print('MXairfoil: tranfer real_to_surrogate. ' + '\nreal state = ' + str(state_real) + '\nsurrogate state = ' + str(surrogate_state))

        fanhuizhi = state_real*1.0
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim] = surrogate_state
        else:
            fanhuizhi[0:self.dim] = surrogate_state
        return fanhuizhi

    def surrogate_to_normal(self,state_surrogate):
        # this is where the differents are
        state_surrogate2,chicun = self.duiqi(state_surrogate)
        normal_obs_space_h =self.normal_obs_space_h[0:self.dim]
        normal_obs_space_l =self.normal_obs_space_l[0:self.dim]
        surrogate_obs_space_h = self.surrogate_obs_space_h[0:self.dim]
        surrogate_obs_space_l = self.surrogate_obs_space_l[0:self.dim]

        surrogate_state_bili = ( surrogate_obs_space_h - surrogate_obs_space_l ) /(normal_obs_space_h - normal_obs_space_l) 
        surrogate_state_c = ( surrogate_obs_space_h + surrogate_obs_space_l ) /2

        normal_state_c = (normal_obs_space_h + normal_obs_space_l)/2
        norm_state = (state_surrogate2 - surrogate_state_c) / surrogate_state_bili + normal_state_c

        if self.tishi > 0:
            print('MXairfoil: tranfer surrogate_to_normal. ' + '\nsurrogate state = ' + str(state_surrogate) + '\nnormal state = ' + str(norm_state))

        fanhuizhi = state_surrogate*1.0
        # fanhuizhi[0:self.dim] = norm_state
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim] = norm_state
        else:
            fanhuizhi[0:self.dim] = norm_state
        return fanhuizhi

    def real_to_normal(self,state_real):
        state_surrogate = self.real_to_surrogate(state_real)
        state_normal = self.surrogate_to_normal(state_surrogate)
        return state_normal

    def normal_to_surrogate(self,state_normal):
        state_normal2,chicun = self.duiqi(state_normal)
        normal_obs_space_h =self.normal_obs_space_h[0:self.dim]
        normal_obs_space_l =self.normal_obs_space_l[0:self.dim]
        surrogate_obs_space_h = self.surrogate_obs_space_h[0:self.dim]
        surrogate_obs_space_l = self.surrogate_obs_space_l[0:self.dim]
        # first, transfer from agent/env([-1,1]) into surrogate([0,1]+_dx)
        bili1 = (surrogate_obs_space_h-surrogate_obs_space_l)/(normal_obs_space_h - normal_obs_space_l)
        zhong_normal = (normal_obs_space_h + normal_obs_space_l)/2
        zhong_surrogate = (surrogate_obs_space_h+surrogate_obs_space_l)/2

        state_surrogate = (state_normal2 - zhong_normal) * bili1 + zhong_surrogate

        if self.tishi > 0:
            print('MXairfoil: tranfer normal_to_surrogate. ' + '\nnormal state = ' + str(state_normal) + '\nsurrogate state = ' + str(state_surrogate))

        fanhuizhi = state_normal*1.0
        
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim] = state_surrogate
        else:
            fanhuizhi[0:self.dim] = state_surrogate
        return fanhuizhi

    def surrogate_to_real(self,state_surrogate):
        # this is to transfer from surrogate([0-dx,1+dx], with virtual grid) to real space 
        # attension, because of virtual grid, this is transfer back form [0,1] to real, despite dx =0.1 
        state_surrogate2,chicun = self.duiqi(state_surrogate)
        real_obs_space_h=self.real_obs_space_h[0:self.dim]
        real_obs_space_l=self.real_obs_space_l[0:self.dim]
        # this is where the differents is
        surrogate_obs_space_h = self.surrogate_obs_space_h[0:self.dim] - self.dx
        surrogate_obs_space_l = self.surrogate_obs_space_l[0:self.dim] + self.dx

        zhong_surrogate = (surrogate_obs_space_h+surrogate_obs_space_l)/2
        bili2 = (real_obs_space_h-real_obs_space_l)/(surrogate_obs_space_h - surrogate_obs_space_l)

        zhong_real = (real_obs_space_h+real_obs_space_l) / 2 

        state_real = (state_surrogate2 - zhong_surrogate) * bili2 +  zhong_real
        if self.tishi > 0:
            print('MXairfoil: tranfer surrogate_to_real. ' + '\nsurrogate state = ' + str(state_surrogate) + '\nreal state = ' + str(state_real))

        fanhuizhi = state_surrogate*1.0
        # fanhuizhi[0:self.dim] = state_real
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim] = state_real
        else:
            fanhuizhi[0:self.dim] = state_real
        return fanhuizhi

    def normal_to_real(self,state_normal):
        state_surrogate = self.normal_to_surrogate(state_normal)
        state_real = self.surrogate_to_real(state_surrogate)
        return state_real

    def real_to_normal_constraints(self,constraints_real):
        chicun = constraints_real.shape
        if len(chicun) > 1:
            # array are inputed.
            constraints_real2 = constraints_real[:,0:self.dim_constraints]
        else:
            constraints_real2 = constraints_real[0:self.dim_constraints]
        zhong_real = (self.real_con_space_h[0:self.dim_constraints]+self.real_con_space_l[0:self.dim_constraints])/2
        bili = (self.normal_con_space_h[0:self.dim_constraints]-self.normal_con_space_l[0:self.dim_constraints])/(self.real_con_space_h[0:self.dim_constraints]-self.real_con_space_l[0:self.dim_constraints])
        zhong_normal = (self.normal_con_space_l[0:self.dim_constraints]+self.normal_con_space_h[0:self.dim_constraints])/2
        constraints_normal = (constraints_real2 - zhong_real) * bili + zhong_normal
        fanhuizhi = constraints_real*1.0
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim_constraints] = constraints_normal
        else:
            fanhuizhi[0:self.dim_constraints] = constraints_normal
        return fanhuizhi

    def normal_to_real_constraints(self,constraints_normal):
        chicun = constraints_normal.shape
        if len(chicun) > 1:
            # array are inputed.
            constraints_normal2 = constraints_normal[:,0:self.dim_constraints]
        else:
            constraints_normal2 = constraints_normal[0:self.dim_constraints]
        zhong_real = (self.real_con_space_h+self.real_con_space_l)/2
        bili = (self.real_con_space_h-self.real_con_space_l)/(self.normal_con_space_h-self.normal_con_space_l)
        zhong_normal = (self.normal_con_space_l+self.normal_con_space_h)/2
        constraints_real = (constraints_normal2 - zhong_normal) * bili + zhong_real 

        fanhuizhi = constraints_normal*1.0
        if len(chicun) > 1:
            # array are inputed.
            fanhuizhi[:,0:self.dim_constraints] = constraints_real
        else:
            fanhuizhi[0:self.dim_constraints] = constraints_real
        return fanhuizhi

    def duiqi(self,state_in):
        # this is to duiqi the dimension.
        chicun = state_in.shape
        if len(chicun) > 1:
            # array are inputed.
            dim_in = chicun[1]
            if self.dim != dim_in:
                print('    transfer: dimension do not match ')
                self.dim = min(self.dim,dim_in)
            state_in2 = state_in[:,0:self.dim]
        else:
            dim_in = chicun[0]
            if self.dim != dim_in:
                print('    transfer: dimension do not match ')
                self.dim = min(self.dim,dim_in)
            state_in2 = state_in[0:self.dim]

        return state_in2*1.0,chicun

if __name__ == '__main__':
    flag = 2
    if flag ==1 :
        # this is for 2D case. NACA65 case precisely.
        shishi = transfer(tishi=1)
        shishi.dim=4 
        # raw_state_normal = np.array([ 0.04078333,-0.03896875,-0.05416667,-0.14924611])  
        # raw_state_surrogate = shishi.normal_to_surrogate(raw_state_normal)
        
        shishi.real_obs_space_l = np.array([0.37,-0.34,0.045,0.35])
        shishi.real_obs_space_h = np.array([0.49,-0.22,0.055,0.45])
        shishi.dx = 0.1 
        original_NACA65_surrogate_state = np.array([0.46570833, 0.45239167, 0.557     , 0.50823   ])
        original_NACA65_real_state = np.array([0.425885, -0.285713, 0.05057 , 0.400823])
        original_NACA65_normal_state = shishi.surrogate_to_normal(original_NACA65_surrogate_state)
        original_NACA65_real_state2 = shishi.surrogate_to_real(original_NACA65_surrogate_state)
        # constraints=np.array([[1.0515,38.0],[1.0509,34.0],[1.0510,34.2],[1.0514,37.1],[1.0513,35.8]])
        # normal_constraints = shishi.real_to_normal_constraints(constraints[3])
        # print(normal_constraints)
        # real_constraints = shishi.normal_to_real_constraints(normal_constraints)
        # print(real_constraints)
        pass
    elif flag == 1.1:
        # this is for CDA1 
        shishi = transfer(tishi=1)
        shishi.dim=4 
        shishi.real_obs_space_h = np.array([0.35,-0.22,0.55,8])
        shishi.real_obs_space_l = np.array([0.25,-0.38,0.35,5])
        shishi.dx = 0.1 
        original_real_state = np.array([0.3024,-0.3037,0.4453,6.2313])
        normal_state = shishi.real_to_normal(original_real_state)
        real_state = shishi.normal_to_real(normal_state)
        pass 
    elif flag ==2:
        # this is for 3D case.
        real_obs_space_h = np.array([0.07,0.14,0.21,0.03,0.06,0.09,0.48,0.15,0.16,0.15,-0.6,-0.02,-0.018,-0.12,0.26,0.7,1,1.15])
        real_obs_space_l = np.array([-0.07,-0.14,-0.21,-0.03,-0.06,-0.09,0.41,0.1,-0.04,-0.05,-0.67,-0.08,-0.08,-0.18,0.18,0.6,0.92,1.05])
        shishi = transfer(tishi=1,dim = 18,real_obs_space_h = real_obs_space_h,real_obs_space_l=real_obs_space_l)
        original_Rotor67_real_state = np.array([0,0,0,0,0,0,0.447895,0.122988,0.064253,0.050306,-0.639794,-0.052001,-0.050454,-0.148836,0.223533,0.656313,0.965142,1.098645])
        original_Rotor67_surrogate_state = shishi.real_to_surrogate(original_Rotor67_real_state)
        original_Rotor67_normal_state = shishi.real_to_normal(original_Rotor67_real_state)
        original_Rotor67_surrogate_state2 = shishi.normal_to_surrogate(original_Rotor67_normal_state)
        original_Rotor67_real_state2 = shishi.surrogate_to_real(original_Rotor67_surrogate_state2)

        state_surogate_BC1 = shishi.surrogate_obs_space_l+shishi.dx
        state_surogate_BC2 = shishi.surrogate_obs_space_h-shishi.dx
        state_normal_BC1 = shishi.surrogate_to_normal(state_surogate_BC1)
        state_normal_BC2 = shishi.surrogate_to_normal(state_surogate_BC2)
        print('MXairfoil: finish checking Rotor67')
        pass

    pass