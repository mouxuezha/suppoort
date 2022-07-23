# trying to call IGG with scripts.
# in fact no need for another .py file.
# 20210407 further modification for parallel.

from gc import collect
import os
import time 
import shutil #this is for operating the folder 
import eventlet #this is for time out
import time_out # this is after all for time out.
import numpy as np

import subprocess 

class call_components:


    def __init__(self,raw_script_folder,raw_matlab_folder,**kargs):
        #initialize. copy folder.
        if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
            #which means in my diannao
            self.IGG_location = 'F:/NUMECA/fine141/bin64'
        elif os.environ['COMPUTERNAME'] == 'DESKTOP-132CR84' :
            # which means in new working zhan.
            self.IGG_location  =  'D:/NUMECA_SOFTWARE/fine141/bin64'
        else:
            # which means in 106 server
            self.IGG_location  =  'C:/NUMECA_SOFTWARE/fineturbo/fine141/bin64'
        

        self.Turbo_location = self.IGG_location
        self.CFView_location = self.IGG_location

        # first, get a name.
        self.raw_script_folder = raw_script_folder
        self.raw_matlab_folder = raw_matlab_folder
        if 'index' in kargs:
            index = kargs['index']
            self.script_folder = raw_script_folder+ str(index)
            self.matlab_location = raw_matlab_folder+ str(index)
        else:
            index = 1 
            i=index
            self.script_folder = raw_script_folder+ str(i)
            while (i<1000)&(os.path.exists(self.script_folder)):
                self.script_folder =  raw_script_folder + str(i)
                i=i+1
                # if there is testCDA1, then use testCDA2
            i=index
            self.matlab_location = raw_matlab_folder+ str(i)
            while (i<1000)&(os.path.exists(self.matlab_location)):
                self.matlab_location =  raw_matlab_folder + str(i)
                i=i+1
                #if there is MXairfoilCDA1, then use MXairfoilCDA2

        if 'source_matlab_folder' in kargs :
            source_matlab_folder = kargs['source_matlab_folder']
        else:
            source_matlab_folder = raw_matlab_folder
        if 'source_script_folder' in kargs :
            source_script_folder = kargs['source_script_folder']
        else:
            source_script_folder = raw_script_folder

        shutil.copytree(source_matlab_folder,self.matlab_location)
        shutil.copytree(source_script_folder,self.script_folder)
        #get something to know done. if it is true, no need to continue.
        self.done = 0

        # #caonima! cao ! 
        # self.set_scripts('testCDA1.py')
        # self.set_scripts('testCDA1_Turbo.py')
        # self.set_scripts('testCDA1_Post.py')
        if 'case' in kargs:
            if kargs['case'] == 'NACA65':
                self.set_locations_NACA65()
            elif kargs['case'] == 'CDA1':
                self.set_locations_CDA1()
            elif kargs['case'] == 'Rotor67':
                self.set_locations_Rotor67()
            elif kargs['case'] == 'Rotor37':
                self.set_locations_Rotor37()

            self.case = kargs['case']
        else:
            self.set_locations_CDA1()
            self.case = 'CDA1'
            self.zhuansu = 0
            self.Pout = 0

        self.X = np.array([0])

    def set_locations_CDA1(self):
        # these location will change according to different object of this class
        # self.script_folder = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'
        # self.matlab_location = 'C:/Users/y/Desktop/MXairfoilCDA'
        self.IGG_script_name = self.script_folder+'/testCDA1.py'
        self.Turbo_script_name = self.script_folder+'/testCDA1_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testCDA1_post.py'
        self.CFView_script_name_huatu = self.script_folder+'/testCDA1_post2.py'

        self.log_location = self.script_folder+'/main/log'
        self.result_folder = self.script_folder+'/testCDA1/jieguo'
        # #caonima! cao ! 
        self.set_scripts('testCDA1.py')
        self.set_scripts('testCDA1_Turbo.py')
        self.set_scripts('testCDA1_Post.py')
        try:
            self.set_scripts('testCDA1_Post2.py')
        except:
            print('MXairfoil: attension! No prepared script for contour huatu!')

    def set_locations_NACA65(self):
        # these location will change according to different object of this class
        # self.script_folder = 'C:/Users/y/Desktop/EnglishMulu/testNACA65'
        # self.matlab_location = 'C:/Users/y/Desktop/MXairfoilNACA65'
        self.IGG_script_name = self.script_folder+'/testNACA65_o.py'
        self.Turbo_script_name = self.script_folder+'/testNACA65_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testNACA65/testNACA65_computation_1/testNACA65_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testNACA65_post.py'
        self.CFView_script_name_huatu = self.script_folder+'/testNACA65_post2.py'

        self.log_location = self.script_folder+'/main/log'
        self.result_folder = self.script_folder+'/testNACA65/jieguo'

        # one call_components object 
        # #caonima! cao ! 
        self.set_scripts('testNACA65_o.py')
        self.set_scripts('testNACA65_Turbo.py')
        self.set_scripts('testNACA65_Post.py')
        try:
            self.set_scripts('testNACA65_Post2.py')
        except:
            print('MXairfoil: attension! No prepared script for contour huatu!')

    def __del__(self):
        #move the ptr out of the temp dir. Or the temp dir can not be deleted.
        try:
            os.chdir(self.raw_matlab_folder)
        except:
            print('MXairfoil: can not move the ptr, for unknow reason')
        #delet temp files here.
        shutil.rmtree(self.matlab_location)
        shutil.rmtree(self.script_folder)
        print('MXairfoil: successfully remove the temp file')

    def clear(self):
        #move the ptr out of the temp dir. Or the temp dir can not be deleted.
        os.chdir(self.raw_matlab_folder)
        #delet temp files here.
        print('MXairfoil: successfully remove the temp file')
        try:
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
        except:
            print('MXairfoil: fail to remove the temp file')
    
    def clear_all(self,raw_script_folder,raw_matlab_folder):
        i=1
        while (i<100):
            clear_script_folder =  raw_script_folder + str(i)
            clear_matlab_location = raw_matlab_folder + str(i)
            if (clear_script_folder != self.script_folder)&(clear_matlab_location != self.matlab_location):
                try:
                    shutil.rmtree(clear_matlab_location)
                    print('MXairfoil: clear_matlab_location successfully')
                except:
                    print('MXairfoil: clear_matlab_location fail, i='+str(i))
                try:
                    shutil.rmtree(clear_script_folder)
                    print('MXairfoil: clear_script_folder successfully')
                except:
                    print('MXairfoil: clear_script_folder fail, i='+str(i))
            # elif clear_script_folder == self.script_folder:

            i=i+1
            #if there is MXairfoilCDA1, then use MXairfoilCDA2
 
    def reset(self):
        # this is to reset the class. Just copy from raw folder again.
        os.chdir(self.raw_matlab_folder) # run out before delet.

        shutil.rmtree(self.matlab_location)
        shutil.rmtree(self.script_folder)
        shutil.copytree(self.raw_matlab_folder,self.matlab_location)
        shutil.copytree(self.raw_script_folder,self.script_folder)
    
    # @time_out.time_out(60, time_out.callback_func)
    def execute_go(self,command):
        #universal command execute, with time out.
        # os.system(command)

        if self.case == 'Rotor67':
            xianshi = 7200 * 2 
        elif self.case == 'Rotor37':
            xianshi =  7200 * 2 
        else: 
            xianshi = 7200 

        # a newer way to call command using subporcess model.
        try:
            jieguo = subprocess.run(command, stdin=None, input=None, stdout=subprocess.DEVNULL, stderr=None, shell=False, timeout=xianshi, check=True)
            #stdout=subprocess.DEVNULL for no output from NUMECA
            #stdout = None for all of the output. using it when debugging.
        except  subprocess.CalledProcessError :
            print('MXairfoil: something really wrong when calling outside process')
            jieguo = 'MXairfoil: running a lonliness'
            # os.system('pause')

        return jieguo.returncode # cannot return subprocess.CompletedProcess, I don't know why. So, returning a returncode.

    # @time_out.time_out(60, time_out.callback_func)
    def call_matlab(self):
        # this is for calling matlab, to get a new airfoil from parameters.
        # exe_location = 'C:/Users/y/Desktop/自动生成几何二维CDA/code'
        self.done = 0
        # print('MXairfoil: debuging multiprocess ')
        # time.sleep(0.5)
        # return 
        matlab_location = self.matlab_location
        matlab_name = matlab_location + '/code/shishi_main4.exe' 
        print('MXairfoil: exe name is: ')
        print(matlab_name)
        os.chdir(matlab_location+'/code')
        flag = os.path.exists(matlab_name)
        if flag == 0:
            print('MXairfoil: did not exist.')
            return 
        mingling = matlab_name + ' '+ matlab_location
        sec_timeout = 100 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(matlab_name)
            jieguo = self.execute_go(mingling)

            if jieguo !=  0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : matlab running a loneliness'+ self.matlab_location
                self.jilu(strbuffer)
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)


        # move the data from matlab to NUMECA
        try:
            if self.case == 'Rotor67':
                os.remove(self.script_folder+'/Rotor67.geomTurbo')
            else:
                os.remove(self.script_folder+'/pressure.dat')
                os.remove(self.script_folder+'/pressure2.dat')
                os.remove(self.script_folder+'/pressure3.dat')
                os.remove(self.script_folder+'/suction.dat')
                os.remove(self.script_folder+'/suction2.dat')
                os.remove(self.script_folder+'/suction3.dat')
        except:
            rizhi ='MXairfoil: unkonwn error when cleanning old airfoil'
            self.jilu(rizhi)
            self.done = 1
            os.system('pause')
        
        try:
            if self.case == 'Rotor67':
                shutil.move(self.matlab_location+'/output/Rotor67.geomTurbo',self.script_folder)
            else:
                shutil.move(self.matlab_location+'/output/'+self.case+'/pressure.dat',self.script_folder)
                shutil.move(self.matlab_location+'/output/'+self.case+'/pressure2.dat',self.script_folder)
                shutil.move(self.matlab_location+'/output/'+self.case+'/pressure3.dat',self.script_folder)
                shutil.move(self.matlab_location+'/output/'+self.case+'/suction.dat',self.script_folder)
                shutil.move(self.matlab_location+'/output/'+self.case+'/suction2.dat',self.script_folder)
                shutil.move(self.matlab_location+'/output/'+self.case+'/suction3.dat',self.script_folder)
        except:
            rizhi ='MXairfoil: unkonwn error when generate airfoil'
            self.jilu(rizhi)
            self.done = 1
            os.system('pause')


        print('MXairfoil: finish generate the airfoil. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(60, time_out.callback_func)
    def call_IGG(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling IGG for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.IGG_location
        exe_name = exe_location + '/iggx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.IGG_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-batch -script' + ' ' + script_name
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            self.done = 1
            return
        
        os.chdir(self.script_folder)
        sec_timeout = 59 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            jieguo = self.execute_go(mingling)

            if jieguo != 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : IGG running a loneliness'+ self.IGG_location
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : IGG time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)

        print('MXairfoil: finish generate the mesh. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(300, time_out.callback_func)
    def call_Turbo(self,**kargs):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling Turbo for something wrong before.'
            self.jilu(rizhi)
            return
        if 'beta' in kargs :
            # which means different angles are going to calculate.
            self.set_scripts(beta=kargs['beta'])
        exe_location = self.Turbo_location
        exe_name = exe_location + '/finex86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.Turbo_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-script' + ' ' + script_name+' -batch'
        # mingling = exe_name + ' '+'-script' + ' ' + script_name
        print('MXairfoil: mingling is: ')
        print(mingling)
        os.chdir(self.script_folder)
        sec_timeout = 59 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            jieguo = self.execute_go(mingling)
            if jieguo!= 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : Turbo running a loneliness'
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : Turbo time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : Turbo time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            mingling = 'taskkill /F /IM finex86_64.exe'
            os.system(mingling)

        print('MXairfoil: finish generate the case. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')   

        #then call euranus to calculate.
        # exe_location = self.Turbo_location
        exe_name = exe_location + '/euranusx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        case_name = self.Turbo_case_name
        print('MXairfoil: case_name name is: ')
        print(case_name)
        mingling = exe_name + ' ' + case_name+' -seq'
        print('MXairfoil: mingling is: ')
        print(mingling)
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(case_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            return
        
        sec_timeout = 9999 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            self.execute_go(mingling)
            if jieguo!= 0:
                # which means turbo exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : euranus running a loneliness'
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : euranus time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()
        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
        
        print('MXairfoil: finish calculate. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(60, time_out.callback_func)
    def call_CFView(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling CFView for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.CFView_location
        exe_name = exe_location + '/cfviewx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.CFView_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-macro' + ' ' + script_name 
        print(mingling)
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            return
        os.chdir(self.script_folder)

        sec_timeout = 59
        time_start = time.time()
        # os.system(mingling)
        jieguo = self.execute_go(mingling)
        if jieguo!= 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : IGG running a loneliness'+ self.IGG_location
                self.jilu(strbuffer)
                return 
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            mingling = 'taskkill /F /IM cfviewx86_64.exe'
            os.system(mingling)

        
        print('MXairfoil: finish post process. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    def call_CFView_huatu(self,**kargs):
        # this is to call CFView and draw contours about 
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling CFView for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.CFView_location
        exe_name = exe_location + '/cfviewx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)

        if 'script_name' in kargs:
            script_name = kargs['script_name']
        else:
            script_name = self.CFView_script_name_huatu
        
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-macro' + ' ' + script_name 
        print(mingling)
        flag = 1
        flag = flag and os.path.exists(exe_name) and os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            return
        os.chdir(self.script_folder)

        sec_timeout = 114.514
        time_start = time.time()
        jieguo = self.execute_go(mingling)
        if jieguo!= 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : CFView running a loneliness'+ self.IGG_location
                self.jilu(strbuffer)
                return 
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            mingling = 'taskkill /F /IM cfviewx86_64.exe'
            os.system(mingling)

        
        print('MXairfoil: finish post process. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

        # also called CFView to get cp data.
        # self.call_CFView()

    def set_step_huatu(self,N_step):
        # set the step in a testCDAx folder, waiting for read operation from testxxx_post2.py
        wenjianming = self.script_folder + '/N_step.txt'
        self.set_value_chouxiang(wenjianming,N_step)

    def save_huatu(self,wenjianjia):
        #save the contour to an assigned 
        shijian = time.strftime("%Y-%m-%d", time.localtime())
        wenjianjia = wenjianjia + '/'+self.case +shijian
        contour_folder = self.script_folder +'/output'
        shutil.copytree(contour_folder,wenjianjia)

    def jilu(self,strBuffer):
        shijian = time.strftime("%Y-%m-%d", time.localtime()) 
        wenjianming = self.log_location+shijian+'.txt'
        rizhi = open(wenjianming,'a')
        rizhi.write(strBuffer+'\n')
        rizhi.write(time.ctime())
        rizhi.write('\n')
        rizhi.close()
        print(strBuffer)
        return
    
    def jilu_data(self,data):
        #store some data.
        shijian = time.strftime("%Y-%m-%d", time.localtime()) 
        wenjianming = self.log_location+shijian+'data.txt'
        wenjian = open(wenjianming,'a')
        wenjian.write(data + '\n')
        wenjian.close()
        return

    def get_value(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling get_value for something wrong before. pause'
            self.jilu(rizhi)
            os.system('pause')
            return 0,0
        result_folder = self.result_folder
        omega_name = result_folder+'/omega.dat'
        rise_name = result_folder+'/rise.dat'
        # turn_name = result_folder+'/turn.dat'
        omega_file = open(omega_name,'r')
        omega= float(omega_file.read())
        omega_file.close()
        rise_file = open(rise_name,'r')
        rise=float(rise_file.read())
        rise_file.close()
        # turn_file = open(turn_name,'r')
        # turn = float(turn_file.read)
        # turn_file.close()

        print('MXairfoil: in this turn, omega = ',omega,'  rise =', rise)
        return omega,rise

    def get_value_new(self):
        #this is for compatibility. no need to change former code.
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling get_value for something wrong before. pause'
            self.jilu(rizhi)
            os.system('pause')
            return 0,0
        result_folder = self.result_folder
        omega_name = result_folder+'/omega.dat'
        rise_name = result_folder+'/rise.dat'
        turn_name = result_folder+'/turning.dat'
        omega_file = open(omega_name,'r')
        omega= float(omega_file.read())
        omega_file.close()
        rise_file = open(rise_name,'r')
        rise=float(rise_file.read())
        rise_file.close()
        turn_file = open(turn_name,'r')
        turn = float(turn_file.read())

        print('MXairfoil: in this turn, omega = ',omega,'  rise =', rise, 'turn =',turn)
        return omega,rise,turn

    def set_value(self,value,value_name):
        value_name=self.matlab_location + '/input/'+self.case+'/'+value_name+'.txt'
        value_file = open(value_name,'w')
        value_file.write(str(value))
        value_file.close()
        shuofa = 'MXairfoil: in this turn, value = '+ str(value)+'  location ='+ value_name
        # self.jilu(shuofa)
        print(shuofa)

    def get_value2(self,value_name):
        value_file = open(value_name,'r')
        value= float(value_file.read())
        value_file.close()
        print('MXairfoil: get the value, value = ',value,'  location =', value_name)
        return value 

    def set_scripts(self,name,**kargs):
        #caonima, gang xiehao ceshihao,jieguo ziji buzaile ,xianzia haiyao chongxin xieyibian, wo tama zhende shi rilegoule cao. caocaocaocaocoacao.
        wenjian = open(self.script_folder+'/'+name,'r')
        neirong = wenjian.read()
        wenjian.close()
        index = neirong.find('\n')
        bianliang_add = 'mulu = \'' + self.script_folder+'\''
        if (name.count('Post')>0) or (name.count('post')>0):
            index = neirong.find('\n',index+1)
            bianliang_add = 'CFViewBackward(1210,) \n'+bianliang_add 
        # if kargs.has_key('beta') : # set angle in Turbo.
        if 'beta' in kargs:
            index = neirong.find('\n',index+1)
            bianliang_add = bianliang_add + 'beta =' + str(kargs['beta'])

        neirong2 = bianliang_add + neirong[index:]
        wenjian = open(self.script_folder+'/'+name,'w')
        wenjian.write(neirong2)
        wenjian.close()

        # print('MXairfoil: caonima!')
        print('MXairfoil: scripts setted!')

    def test_existing_case(self,i,**kargs):
        #just test existing case.
        self.matlab_location = self.raw_matlab_folder + str(i)
        self.script_folder =  self.raw_script_folder + str(i)
        if 'case' in kargs:
            if kargs['case'] == 'NACA65':
                self.set_locations_NACA65()
            elif kargs['case'] == 'CDA1':
                self.set_locations_CDA1()
            elif kargs['case'] == 'Rotor67':
                self.set_locations_Rotor67()
                self.zhuansu = -16173
                self.Pout = 128591.6 
                self.massflow_deviation_threshold=0.5
                self.massflow_0 = 34.6
                self.efficiency_threshold=0.87

            self.case = kargs['case']
    
    def del_gai(self):
        try:
            #move the ptr out of the temp dir. Or the temp dir can not be deleted.
            os.chdir(self.raw_matlab_folder)
            #delet temp files here.
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            print('MXairfoil: successfully remove the temp file using del_gai in call_components')
        except OSError as e:
            print('MXairfoil: fail to remove the temp file in del_gai in call_components')
            print(e)
    def reset(self):
        # this is to reset the class. Just copy from raw folder again.
        os.chdir(self.raw_matlab_folder) # run out before delet.
        try:
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            shutil.copytree(self.raw_matlab_folder,self.matlab_location)
            shutil.copytree(self.raw_script_folder,self.script_folder)
        except:
            strbuffer = 'MXairfoil: cannot reset. fail to remove the temp file. \n' + self.matlab_location + '\n'+self.script_folder
            self.jilu(strbuffer)
            # shutil.copytree(self.raw_matlab_folder,self.matlab_location)
            # shutil.copytree(self.raw_script_folder,self.script_folder)
            # avoid deleting part of file 
    
    # here we start 3D case, incremental updating
    def set_locations_Rotor67(self):
        self.IGG_script_name = self.script_folder+'/testRotor67.py'
        self.Turbo_script_name = self.script_folder+'/testRotor67_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testRotor67_post.py'
        self.CFView_script_name_huatu = self.script_folder+'/testRotor67_post2.py'

        self.log_location = self.script_folder+'/main/log'
        self.result_folder = self.raw_script_folder+'/main/jieguo'
        self.Turbo_set_location = self.script_folder + '/Turbo_set'
        self.Turbo_mf_name = self.script_folder+'/testRotor67/testRotor67_computation_1/testRotor67_computation_1.mf'

        # one call_components object 
        # #caonima! cao ! 
        self.set_scripts('testRotor67.py')
        self.set_scripts('testRotor67_Turbo.py')
        # self.set_scripts('testRotor67_Post.py')

        self.zhuansu = -16173
        self.Pout = 128591.6 
        self.massflow_deviation_threshold=0.5
        self.massflow_0 = 34.6
        self.efficiency_threshold=0.87


    # another 3D case, for validat CFD tools.
    def set_locations_Rotor37(self):
        self.IGG_script_name = self.script_folder+'/testRotor37.py'
        self.Turbo_script_name = self.script_folder+'/testRotor37_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testRotor37/testRotor37_computation_1/testRotor37_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testRotor37_post.py'
        self.CFView_script_name_huatu = self.script_folder+'/testRotor37_post2.py'

        self.log_location = self.script_folder+'/main/log'
        self.result_folder = self.raw_script_folder+'/main/jieguo'
        self.Turbo_set_location = self.script_folder + '/FlowSetting'
        self.Turbo_mf_name = self.script_folder+'/testRotor37/testRotor37_computation_1/testRotor37_computation_1.mf'

        # one call_components object 
        # #caonima! cao ! 
        self.set_scripts('testRotor37.py')
        self.set_scripts('testRotor37_Turbo.py')
        # self.set_scripts('testRotor37_Post.py')        

        self.zhuansu = -17188
        self.Pout = 120000 
        self.massflow_deviation_threshold=0.5
        self.massflow_0 = 20.83
        self.efficiency_threshold=0.87

    def call_AutoGrid5(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling AutoGrid5 for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.IGG_location
        exe_name = exe_location + '/iggx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.IGG_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' -autogrid5 -batch -script ' + script_name
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            self.done = 1
            return
        
        os.chdir(self.script_folder)
        time_start = time.time()
        try:
            jieguo = self.execute_go(mingling)
        except :
            # which means matlab exits with exception
            self.done = 1
            strbuffer = 'MXairfoil : AutoGrid5 running a loneliness'+ self.IGG_location
            self.jilu(strbuffer)
            return
        time_end = time.time()
        print('MXairfoil: finish generate the mesh. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    def check_result_time(self,run_location,mf_location):
        # just compare two file, if they are created at different date, 
        # then this CFD point is fail,return F.
        # run_ctime = os.path.getctime(run_location)
        # mf_ctime = os.path.getctime(mf_location)
        run_mtime = os.path.getmtime(run_location)
        mf_mtime = os.path.getmtime(mf_location)
        shijiancha =  abs(mf_mtime - run_mtime)
        if shijiancha > 7200*12:
            # 114514 s = 31 h.
            print('MXairfoil: one of the CFD points GGed, mf_location=' + mf_location)
            zhi = False
            pass 
        else:
            zhi = True
        return zhi 

    def get_result_3D(self,**kargs):
        ################################################################
        ## get the global performance from *.mf, save in a convenient place to use.
        ################################################################
        # working = self.result_folder # this is for total result
        working = self.script_folder + '/main/jieguo' # this is for local, temp Result.txt
        if 'target' in kargs:
            working = kargs['target'] + '/main/jieguo'
        if 'resultLocation' in kargs:
            resultLocation = kargs['resultLocation']
            if self.case == 'Rotor67':
                runLocation = resultLocation + '/testRotor67/testRotor67_computation_1/testRotor67_computation_1.run'
                resultLocation = resultLocation + '/testRotor67/testRotor67_computation_1/testRotor67_computation_1.mf'
            elif self.case == 'Rotor37':
                runLocation = resultLocation + '/testRotor37/testRotor37_computation_1/testRotor37_computation_1.run'
                resultLocation = resultLocation + '/testRotor37/testRotor37_computation_1/testRotor37_computation_1.mf'
            else:
                raise Exception('MXairfoil: invalid settings when getting result')
        else:
            runLocation = self.Turbo_case_name
            resultLocation = self.Turbo_mf_name

        check_timeout = self.check_result_time(runLocation,resultLocation)
        if check_timeout :
            pass 
        else:
            # this CFD point has GGed 
            liuliang_zuobi = self.massflow_0*0.5 
            piStar_zuobi = 1.0
            eta_i_zuobi = 0.7777777
            return liuliang_zuobi,piStar_zuobi,eta_i_zuobi


        zhuansu = self.get_value2(self.Turbo_set_location + '/rotational_speed.txt')
        globalPerformance = open(resultLocation,"r")
        strBuffer = globalPerformance.read()
        # print(strBuffer)
        # finish reading file, then apply some str process.
        shishi=strBuffer.split('Mass_flow')
        shishi=shishi[1].split('[kg/s]')
        shishi=shishi[0].strip()
        massFlow=shishi.split('             ') #massFlow = [massflow_inlet massflow_outlet]
        # print(massFlow)

        # then get Absolute_total_pressure_ratio
        shishi=strBuffer.split('Absolute_total_pressure_ratio')
        shishi=shishi[1].split('\n')
        piStar = shishi[0]

        # then get Absolute_total_temperature_ratio
        shishi=strBuffer.split('Absolute_total_temperature_ratio')
        shishi=shishi[1].split('\n')
        thetaStar = shishi[0]
        # print(thetaStar)

        # then get Isentropic_efficiency
        shishi=strBuffer.split('Isentropic_efficiency')
        shishi=shishi[1].split('(')
        eta_i = shishi[0]
        # print(eta)

        # then get Polytropic_efficiency
        shishi=strBuffer.split('Polytropic_efficiency')
        shishi=shishi[1].split('\n')
        eta_p = shishi[0]
        # print(eta)

        globalPerformance.close()

        # then concentrate these data, add into one file 
        totalResult = open(working+'/Result.txt','a')
        zhuansu = str(zhuansu)
        totalResult.write(zhuansu+'\t'+massFlow[0]+'\t'+ massFlow[1]+'\t'+piStar+'\t'+thetaStar+'\t'+eta_i+'\t'+eta_p+'\n')
        totalResult.close()

        print("MXairfoil: finish get the result of one")
        liuliang = 0.5*(float(massFlow[0])+float(massFlow[1]))
        return liuliang,piStar,eta_i

    def set_zhuansu(self,zhuansu):
        # this is for 3D case, set zhuasnu.
        if zhuansu> 0:
            zhuansu = -1.0* zhuansu
        self.zhuansu = zhuansu
        value_name=self.Turbo_set_location + '/rotational_speed.txt'
        self.set_value_chouxiang(value_name,self.zhuansu)
        shuofa = 'MXairfoil: in this turn, zhuansu = '+ str(self.zhuansu)+'  location ='+ value_name
        print(shuofa)
    
    def set_Pout(self,Pout):
        # this is for 3D case, set outlet pressure.
        self.Pout = Pout
        value_name=self.Turbo_set_location + '/Static_Pressure.txt'
        self.set_value_chouxiang(value_name,self.Pout)
        shuofa = 'MXairfoil: in this turn, Pout = '+ str(self.Pout)+'  location ='+ value_name
        print(shuofa)

    def set_value_chouxiang(self,name,value):
        # a more universal set_value file.
        value_file = open(name,'w')
        value_file.write(str(value)) 
        value_file.close()
        return

    def set_value_mul(self,name,value,index):
        # this is to set inputs which have more than one value
        # index is something like [2,1].
        data = np.loadtxt(name)
        data[index[0]][index[1]] = value 
        np.savetxt(name,np.c_[data],fmt='%f',delimiter='\t')

    def set_value_3D(self,X):
        # this is no longer directly.X is in real space.
        location = self.matlab_location+'/input/ThreeD'
        self.X = X 

        # check the X.
        chicun = X.shape
        if chicun[0] != 18:
            raise Exception('MXairfoil: invalid X for set_value_3D')

        index = 0 
        # first, span_dm  
        for i in range(3):
            name = location+'/span_dm.txt'
            self.set_value_mul(name,X[index],[i+1,1]) 
            index = index+1
        # then, spand_dtheta
        for i in range(3):
            name = location+'/span_dtheta.txt'
            self.set_value_mul(name,X[index],[i+1,1])
            index = index+1
        # then, chi_in
        for i in range(4):
            name = location + '/chi_in.txt'
            self.set_value_mul(name,X[index],[i,1])
            index = index+1
        # then, chi_out
        for i in range(4):
            name = location +'/chi_out.txt'
            self.set_value_mul(name,X[index],[i,1])
            index = index+1 
        # then, zeta
        for i in range(4):
            name = location + '/zeta.txt'
            self.set_value_mul(name,X[index],[i,1])
            index = index +1

    def result_process_3D(self,**kargs):
        # 1, read from Reasult.txt, and calculate mass flow rate.
        # working = self.result_folder # this is for total result
        working = self.script_folder + '/main/jieguo' # this is for 
        if 'name' in kargs:
            totalResult = working+kargs['name']
        else:
            totalResult = working+'/Result.txt'
        data = np.loadtxt(totalResult)
        # rpm,massflow_in,massflow_out,Absolute_total_pressure_ratio,Isentropic_efficiency,Polytropic_efficiency.
        # massflow_0 = 34.6 # kg/s
        massflow_0 = self.massflow_0
        massflow_ave = 0.5*(data[:,1]+data[:,2]) 
        massflow_rate = massflow_ave / massflow_0 
        massflow_deviation = abs(data[:,1]-data[:,2])
        data2 = np.insert(data,7,massflow_rate,axis =1) 
        data2 = np.insert(data2,8,massflow_deviation,axis =1) 
        
        # 2, sort through mass flow rate, and filter the data.
        # massflow_deviation_threshold=1 # 0.3 is too low, only for original.
        massflow_deviation_threshold=self.massflow_deviation_threshold
        data3 = data2[data2[:, 7].argsort()]
        # data2 = np.flipud(data2)
        data3 = data3[data3[:,8]<massflow_deviation_threshold]

        # 3, fit these data into a curve.
        # curve for efficiency,x-massflow_rate,y-efficiency        
        data_efficiency = np.array([data3[:,7],data3[:,6]])
        data_efficiency = data_efficiency.T
        curve_efficiency = curve(data_efficiency,x_name='massflow_rate',y_name='efficiency',title='efficiency')
        data_pi = np.array([data3[:,7],data3[:,3]])
        data_pi = data_pi.T
        curve_pi = curve(data_pi,x_name='massflow_rate',y_name='pi',title='pi'
        )

        # 4, integration and give result.
        # efficiency_threshold = 0.87 # 0.88 might be too high. 
        efficiency_threshold=self.efficiency_threshold
        zhi = curve_efficiency.y_to_x(efficiency_threshold) # there should be two x

        try:
            massflow_rate_lower = zhi[0] 
            massflow_rate_upper = zhi[1]
        except:
            # if no area to integral
            massflow_rate_lower = min(data_efficiency[0,:])
            massflow_rate_upper = max(data_efficiency[0,:])
            efficiency_integration = 0 
            pi_integration = 0 
            return massflow_rate_lower,massflow_rate_upper,efficiency_integration,pi_integration

        efficiency_integration = curve_efficiency.integral(massflow_rate_lower,massflow_rate_upper)
        pi_integration = curve_pi.integral(massflow_rate_lower,massflow_rate_upper)

        return massflow_rate_lower,massflow_rate_upper,efficiency_integration,pi_integration
    
    def reset_result_3D(self,**kargs):
        # clear the Result.txt, and move the neirong into main 
        # 1,get the data from local temp Result.txt
        location = self.script_folder + '/main/jieguo/Result.txt'
        totalResult = open(location,'r') 
        data = np.loadtxt(totalResult)
        totalResult.close()
        
        if 'collect' in kargs:
            # 2, write them into a total result Result.txt
            location_total = self.result_folder + '/Result_all.txt'
            totalResult = open(location_total,'a+')
            totalResult.write('\nX='+str(self.X)+'\n')
            totalResult.write(str(data))
            np.savetxt(totalResult,np.c_[data],fmt='%f',delimiter='\t')
            totalResult.close()      
        

        # 3,clear the local temp Result.txt
        if 'clear' in kargs:
            pass
        else:
            totalResult = open(location,'w') 
            totalResult.close()          

    # ===========================================
    def call_CFview_lumped(self,location_storage,location_lumped,label=''):
        # get script from one location, then post huatu, then copy to lumped location.
        self.location_lumped = location_lumped 
        #1, copy case file from location_storage
        self.get_stoarged_case(location_storage)

        # 2, load extra post scripts from location_lumped
        script_list = self.load_extra_scripts(location_lumped)

        # 3, then, huatu_post
        for script_single in script_list:
            try:
                self.call_CFView_huatu(script_name = script_single)
            except:
                print('MXairfoil: G when running '+script_single)

        # 4, then, collect the jieguo back.
        self.collect_jieguo(location_lumped=location_lumped,label=label)

    def collect_jieguo(self,location_lumped,label=''):
        jieguo_folder = self.script_folder+'/main/jieguo'
        jieguo_new = location_lumped+'/jieguo'+label
        if (os.path.isfile(jieguo_folder)==True) and (os.path.isfile(jieguo_new)==False) :
            shutil.copytree(jieguo_folder,jieguo_new)
        else:
            raise Exception('MXairofil: invalid location when collect_jieguo')
        pass 

    def load_extra_scripts(self,location_lumped):
        # 
        script_list = [] 
        for file in os.listdir(location_lumped):
            if file.find('.py') != -1 : 
                # which means this file is a python script.
                file_name_old = os.path.join(location_lumped,file)
                file_name_new = os.path.join(self.script_folder,file)
                shutil.copy(file_name_old,file_name_new)
                self.set_scripts(file)
                script_list.append(file_name_new)

        return script_list
                
    def get_stoarged_case(self,location_storage):
        # #1, copy case file from location_storage, and some necessarry adjustment
        if os.path.exists(location_storage):
            pass
        else:
            raise Exception('MXairfoil: no such case to load, '+location_storage)
        shutil.rmtree(self.script_folder)
        self.script_folder = self.get_storaged_case_dizhi(location_storage)
        shutil.copytree(location_storage,self.script_folder)        
        if self.case == 'NACA65':
            self.set_locations_NACA65()
        elif self.case == 'CDA1':
            self.set_locations_CDA1()
        elif self.case == 'Rotor67':
            self.set_locations_Rotor67()
        elif self.case == 'Rotor37':
            self.set_locations_Rotor37()
        
        print('MXairfoil: storaged case loaded, ' + location_storage)

    def get_storaged_case_dizhi(self,location_storage):
        # load a .py file to get dizhi.
        for file in os.listdir(location_storage):
            if file.find('_Turbo.py') != -1 : 
                # which means this is Turbo script.
                wenjian = open(location_storage+'/'+file,'r')
                neirong = wenjian.read()
                wenjian.close()
                index = neirong.find('\n')
                mulu_str = neirong[0:index]
                mulu_str = mulu_str.replace('mulu = ','')
                mulu_str = mulu_str.replace("'",'')
                break
        if os.path.exists(mulu_str):
            raise Exception('MXairfoil: folder exists ' +mulu_str)
            
        print('MXairfoil: script folder loaded from storaged case: \n'+mulu_str)
        return mulu_str
                

class curve():
    def __init__(self,data,**kargs) -> None:
        # paixu.
        data = data[np.argsort(data[:,0]),:]
        self.data =np.flipud( data) # this is x-y inputed
        
        if 'x_name' in kargs:
            self.x_name = kargs['x_name']
        else:
            self.x_name = 'x_name'
        if 'y_name' in kargs:
            self.y_name = kargs['y_name']
        else:
            self.y_name = 'y_name'
        if 'title' in kargs:
            self.title = kargs['title']
        else:
            self.title = 'simple line'
        pass

    def y_to_x(self,y):
        # given y, interpolate and get x.
        chicun = self.data.shape 
        zhi = np.array([])
        if chicun[0] == 0:
            # which means no data for this curve, then return empty.
            return zhi 
        for i in range(chicun[0]-1):
        # for lie in self.data:
            # lie = self.data[i]
            if ((y>=self.data[i,1])&(y<self.data[i+1,1])):
                # too simple, sometimes naive.
                # for raising curve.
                x_result = (self.data[i+1,0] - self.data[i,0])*(y - self.data[i,1])/(self.data[i+1,1] - self.data[i,1])+self.data[i,0] # (x-x)/(y-y)=(x-x)/(y-y)
                zhi = np.append(zhi,x_result)
            elif ((y<=self.data[i,1])&(y>self.data[i+1,1])):
                # for declining curve. 
                x_result = (self.data[i+1,0] - self.data[i,0])*(y - self.data[i,1])/(self.data[i+1,1] - self.data[i,1])+self.data[i,0] # (x-x)/(y-y)=(x-x)/(y-y)
                zhi = np.append(zhi,x_result)
            elif ((y==self.data[i,1])&(y==self.data[i+1,1])):
                # for horizontal line.
                x_result = 0.5*(self.data[i+1,0] + self.data[i,0]) 
                zhi = np.append(zhi,x_result)

        if y<self.data[0,1]: # for very small y
            vector = self.data[0,:]-self.data[1,:] ; 
            bili = (y - self.data[1,1])/(self.data[0,1] - self.data[1,1])
            zhongdian = self.data[1,:] + vector * bili 
            x_result = zhongdian[0] ; 
            zhi = np.append(zhi,x_result)
        if y<self.data[chicun[0]-1,1]: # for very small y, another direction.
            vector = self.data[chicun[0]-1,:]-self.data[chicun[0]-2,:] ; 
            bili = (y - self.data[chicun[0]-2,1])/(self.data[chicun[0]-1,1] - self.data[chicun[0]-2,1])
            zhongdian = self.data[chicun[0]-2,:] + vector * bili 
            x_result = zhongdian[0] ; 
            zhi = np.append(zhi,x_result)
        return zhi 

    def x_to_y(self,x):
        # this is single valued.
        # given x, interpolate and get y.
        chicun = self.data.shape 
        zhi = np.array([])
        if chicun[0] == 0:
            # which means no data for this curve, then return empty.
            return zhi 

        if x<=min(self.data[0,0],self.data[chicun[0]-1,0]): # for very small x
            # vector = self.data[0,:]-self.data[1,:] ; 
            # bili = (x - self.data[1,0])/(self.data[0,0] - self.data[1,0]) # mo jian chu
            # zhongdian = self.data[1,:] + vector * bili 
            # y_result = zhongdian[1] ; 
            y_result = 0 
            zhi = np.append(zhi,y_result)
        elif x>=max(self.data[0,0],self.data[chicun[0]-1,0]): # for bigger x.
            # vector = self.data[chicun[0]-1,:]-self.data[chicun[0]-2,:] ; 
            # bili = (x - self.data[chicun[0]-2,0])/(self.data[chicun[0]-1,0] - self.data[chicun[0]-2,0])
            # zhongdian = self.data[chicun[0]-2,:] + vector * bili 
            # y_result = zhongdian[1] ; 
            y_result = self.data[0,0]
            zhi = np.append(zhi,y_result) 
        else:
            for i in range(chicun[0]-1):
                if ((x>=self.data[i,0])&(x<self.data[i+1,0])):
                    # too simple, sometimes naive.
                    y_result = (self.data[i+1,1] - self.data[i,1])*(x - self.data[i,0])/(self.data[i+1,0] - self.data[i,0])+self.data[i,1] # (y-y)/(x-x)=(y-y)/(x-x)
                    zhi = np.append(zhi,y_result)
                elif ((x==self.data[i,0])&(x==self.data[i+1,0])):
                    y_result = 0.5*(self.data[i+1,1] + self.data[i,1])
                    zhi = np.append(zhi,y_result)
                elif ((x<self.data[i,0])&(x>=self.data[i+1,0])):
                    # another direction.
                    y_result = (self.data[i+1,1] - self.data[i,1])*(x - self.data[i,0])/(self.data[i+1,0] - self.data[i,0])+self.data[i,1] # (y-y)/(x-x)=(y-y)/(x-x)
                    zhi = np.append(zhi,y_result)

        
        if (len(zhi)>1)or(np.isnan(zhi))or(np.isnan(x)):
            raise Exception('MXairfoil: x_to_y wrong in class curve')
        return zhi[0]        

    def integral(self,x_xia,x_shang):
        # this is a simple integration operation.
        N = 300 
        dx = (x_shang - x_xia)/N 
        # check the data # no longer check.
        # if (max(x_shang,x_xia)>max(self.data[:,0]))or(min(x_shang,x_xia)<min(self.data[:,0])):
        #     # (&,|) and (and,or) is not the same, but the same.
        #     raise Exception('MXairfoil: invalid integration range, G! ')
        #     # print('MXairfoil: invalid integration range, G! ')
        # then calculate integration.
        x_process = x_xia
        jieguo = 0.0 
        for i in range(N):
            jieguo = jieguo + dx*0.5*(self.x_to_y(x_process)+self.x_to_y(x_process+dx))
            x_process = x_process + dx
        return jieguo 

    def visual(self):
        # just plot the curve
        from huatu import huatu
        tu = huatu(self.data) 
        tu.huatu2()


if __name__=="__main__":
    # this is for test the temp file.
    # script_folder = 'C:/Users/y/Desktop/temp/testCDA1'
    # matlab_location = 'C:/Users/y/Desktop/temp/MXairfoilCDA'

    if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
        #which means in my diannao
        # script_folder = 'C:/Users/y/Desktop/temp/testNACA65'
        # matlab_location = 'C:/Users/y/Desktop/temp/MXairfoilNACA65'
        script_folder = 'C:/Users/y/Desktop/EnglishMulu/testRotor67'
        matlab_location = 'C:/Users/y/Desktop/EnglishMulu/MXairfoilRotor67'
    elif os.environ['COMPUTERNAME'] == 'DESKTOP-132CR84' :
        # which means in new working zhan.
        # D:\XXHdatas\EnglishMulu
        script_folder = 'D:/XXHdatas/EnglishMulu/testRotor67'
        matlab_location = 'D:/XXHdatas/EnglishMulu/MXairfoilRotor67'        
    else:
        # which means in 106 server
        script_folder = 'C:/Users/106/Desktop/EnglishMulu/testNACA65'
        matlab_location = 'C:/Users/106/Desktop/EnglishMulu/MXairfoilNACA65'
    shishi = call_components(script_folder,matlab_location,case='Rotor67')
    # shishi = 'debug'
    flag = -999
    if flag == 0 :
        #do one loop of the CFD
        # shishi.call_matlab()
        # shishi.call_IGG()
        # shishi.call_Turbo()
        # shishi.call_CFView()
        omega,rise = shishi.get_value()
        omega,rise,turn = shishi.get_value_new()
        # shishi.jilu_data(str([omega,rise]))
        del shishi
    elif flag == 1 :
        chi_in = shishi.get_value2(shishi.matlab_location+'/input/CDA1/chi_in.txt')
        chi_out = shishi.get_value2(shishi.matlab_location+'/input/CDA1/chi_out.txt')
        mxthk = shishi.get_value2(shishi.matlab_location+'/input/CDA1/mxthk.txt')
        umxthk = shishi.get_value2(shishi.matlab_location+'/input/CDA1/umxthk.txt')
        
        shishi.set_value(8,'umxthk')
        # shishi.set_value(x_rand[1],'chi_out')
        # shishi.set_value(x_rand[2],'mxthk')
        # shishi.set_value(x_rand[3],'umxthk')
        shishi.call_matlab()
        shishi.call_IGG()
        shishi.call_Turbo()
        shishi.call_CFView()        
        omega,rise = shishi.get_value_new()
    elif flag == 2 :
        shishi.test_existing_case(7)
        shishi.call_matlab()
        shishi.call_IGG()
        shishi.call_Turbo()
        shishi.call_CFView()        
        omega,rise = shishi.get_value()
        rizhi = 'MXairfoil: struggle to find out bug..'+'\n '+shishi.result_folder + '\n  ' + str(omega)+'    ' + str(rise)  
        shishi.jilu(rizhi)
    elif flag == 3:
        # test the components, for 3D case such as NASA Rotor 67.
        # shishi.call_AutoGrid5()
        # shishi.get_result_3D()
        shishi.call_Turbo()
        name = r'C:\Users\y\Desktop\Rotor67_new\input\ThreeD\span_dm.txt'
        shishi.set_value_mul(name,0.123,[1,2]) 
    elif flag == 4 :
        # get results from Result.txt
        massflow_rate_lower,massflow_rate_upper,efficiency_integration,pi_integration=shishi.result_process_3D() 
        shishi.reset_result_3D(collect=True)
        shishi.clear_all(script_folder,matlab_location)
    elif flag == 5 :
        # test things about contour huatu.
        script_folder = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'
        matlab_location = 'C:/Users/y/Desktop/EnglishMulu/MXairfoilCDA'
        shishi = call_components(script_folder,matlab_location,case='CDA1')
        shishi.set_step_huatu(114514)
        shishi.save_huatu('C:/Users/y/Desktop/EnglishMulu/figure-post')
        shishi.clear_all(script_folder,matlab_location)
    elif flag == 7 : 
        # this is to debug Rotor 67
        shishi2 = call_components(script_folder,matlab_location,case='Rotor67',index=10)
        shishi2.get_result_3D()
    elif flag == -999:
        # clear all temp files
        # shishi = call_components(script_folder,matlab_location)
        shishi.clear_all(script_folder,matlab_location)
        del shishi
    print('MXairfoil: debuging call_components')


