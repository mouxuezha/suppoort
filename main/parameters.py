# get a enum class to save the parameter information
from enum import Enum
class parameters(Enum):
    chi_in = 0 
    chi_out = 1
    mxthk = 2 
    umxthk = 3
    def get_number():
        n=0 
        for shishi in parameters:
            n=n+1
        return n
    def get_equation(duixiang,**kargs):
        # this is to get equation.
        if 'normal' in kargs:
            if kargs['normal'] == True:
                if(duixiang.value == 0 ):
                    equation = r'$\hat{\chi}_{in}$' 
                elif(duixiang.value == 1):
                    equation = r'$\hat{\chi}_{out}$'
                elif(duixiang.value == 2):
                    equation = r'$\hat{t}_{max}$'
                elif(duixiang.value == 3):
                    equation = r'$\hat{u}_{tm}$'
                else:
                    equation = 'MXairfoil: something wrong in parameter enum' 
        else:               
            if(duixiang.value == 0 ):
                equation = r'$\chi_{in}$'
            elif(duixiang.value == 1):
                equation = r'$\chi_{out}$'
            elif(duixiang.value == 2):
                equation = r'$t_{max}$'
            elif(duixiang.value == 3):
                equation = r'$u_{tm}$'
            else:
                equation = 'MXairfoil: something wrong in parameter enum'
        
        return equation

class parameters_Rotor67_state(Enum):
    span_dm_1 = 0 
    span_dm_2 = 1
    span_dm_3 = 2 
    span_dtheta_1 = 3
    span_dtheta_2 = 4
    span_dtheta_3 = 5
    chi_in_1 = 6
    chi_in_2 = 7
    chi_in_3 = 8
    chi_in_4 = 9
    chi_out_1 = 10
    chi_out_2 = 11
    chi_out_3 = 12
    chi_out_4 = 13
    zeta_1 = 14
    zeta_2 = 15
    zeta_3 = 16
    zeta_4 = 17
    def get_number():
        n=0 
        for shishi in parameters:
            n=n+1
        return n

    def get_equation(duixiang,**kargs):
        # this is to get equation.
        equation_normal_list = [] 
        equation_list = []

        equation_normal_list.append(r'$\it{\hat{dm}_{r,1}}$') 
        equation_normal_list.append(r'$\it{\hat{dm}_{r,2}}$') 
        equation_normal_list.append(r'$\it{\hat{dm}_{r,3}}$') 
        equation_normal_list.append(r'$\it{\hat{d\theta}_{r,1}}$') 
        equation_normal_list.append(r'$\it{\hat{d\theta}_{r,2}}$') 
        equation_normal_list.append(r'$\it{\hat{d\theta}_{r,3}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{in,1}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{in,2}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{in,3}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{in,4}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{out,1}}$')
        equation_normal_list.append(r'$\it{\hat{\chi}_{out,2}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{out,3}}$') 
        equation_normal_list.append(r'$\it{\hat{\chi}_{out,4}}$')
        equation_normal_list.append(r'$\it{\hat{\zeta}_{1}}$')
        equation_normal_list.append(r'$\it{\hat{\zeta}_{2}}$')
        equation_normal_list.append(r'$\it{\hat{\zeta}_{3}}$')
        equation_normal_list.append(r'$\it{\hat{\zeta}_{4}}$')

        equation_list.append(r'$\it{dm_{r,1}}$') 
        equation_list.append(r'$\it{dm_{r,2}}$') 
        equation_list.append(r'$\it{dm_{r,3}}$') 
        equation_list.append(r'$\it{d\theta_{r,1}}$') 
        equation_list.append(r'$\it{d\theta_{r,2}}$') 
        equation_list.append(r'$\it{d\theta_{r,3}}$') 
        equation_list.append(r'$\it{\chi_{in,1}}$') 
        equation_list.append(r'$\it{\chi_{in,2}}$') 
        equation_list.append(r'$\it{\chi_{in,3}}$') 
        equation_list.append(r'$\it{\chi_{in,4}}$') 
        equation_list.append(r'$\it{\chi_{out,1}}$')
        equation_list.append(r'$\it{\chi_{out,2}}$') 
        equation_list.append(r'$\it{\chi_{out,3}}$') 
        equation_list.append(r'$\it{\chi_{out,4}}$')
        equation_list.append(r'$\it{\zeta_{1}}$')
        equation_list.append(r'$\it{\zeta_{2}}$')
        equation_list.append(r'$\it{\zeta_{3}}$')
        equation_list.append(r'$\it{\zeta_{4}}$')
        if 'normal' in kargs:
            normal = kargs['normal']
        else:
            normal = True
        if normal:
            equation = equation_normal_list[duixiang.value]
        else:
            equation = equation_list[duixiang.value]
        
        return equation

class parameters_Rotor67_performance(Enum):
    massflow_rate_lower = 0 
    massflow_rate_upper = 1
    efficiency_integration = 2 
    pi_integration = 3
    massflow_rate_w = 4
    eta_w = 5
    pi_w = 6
    def get_number():
        n=0 
        for shishi in parameters:
            n=n+1
        return n     
    def get_equation(duixiang,**kargs):
        # this is to get equation.
        equation_normal_list = [] 
        equation_list = []

        equation_normal_list = [r'\dot{m}_{l}',r'\dot{m}_{u}',r'\eta_{i}',r'\pi_{i}',r'\dot{m}_{w}',r'\eta_{w}',r'\pi_{w}'] 
 

        if 'normal' in kargs:
            normal = kargs['normal']
        else:
            normal = True
        if normal:
            equation = equation_normal_list[duixiang.value]
        else:
            raise Exception('MXairfoil: invalid use of parameters_Rotor67_performance')
        
        return equation

if __name__ == '__main__':
    #test the enum class 
    # shishi = parameters['chi_out']
    shishi2 = parameters_Rotor67_state['span_dm_3'].value*2 +114514 
    for shishi in parameters_Rotor67_state:
        # print(shishi)
        print(shishi.name)
        print(shishi.value)
        print(parameters_Rotor67_state.get_equation(shishi))

    print(parameters_Rotor67_state.get_number())
    # shishi = '$'+parameters(1).name+'$'
    # print(shishi)
    shishi = parameters_Rotor67_performance(1)
    print(shishi)

