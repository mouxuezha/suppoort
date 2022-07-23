# get e script to refresh the call_componnets in shishimujoco.

import os
import time 
import shutil #this is for operating the folder 

class refresh():

    def __init__(self) -> None:
        if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
        # which means in my diannao
            self.script_folder = 'C:/Users/y/Desktop/DDPGshishi/main'
            self.target_folder = 'F:/anaconda3/envs/shishimujoco/Lib'
            self.target_folder = 'F:/anaconda3/envs/shishigpu/Lib'
        elif os.environ['COMPUTERNAME'] == 'DESKTOP-132CR84' :
        # which means in new working zhan.
        # D:\XXHTtools\envs\shishinew # D:\XXHcode\DDPGshishi
            self.script_folder = 'D:/XXHcode/DDPGshishi/main'
            self.target_folder = 'D:/XXHTtools/envs/shishinew/Lib'
        pass
    def go_file(self):
        # os.remove(self.target_folder+'/call_components.py')
        shutil.copyfile(self.script_folder+'/call_components.py' , self.target_folder+'/call_components.py')
        shutil.copyfile(self.script_folder+'/time_ratio.py' , self.target_folder+'/time_ratio.py')
        shutil.copyfile(self.script_folder+'/huatu.py' , self.target_folder+'/huatu.py')
        shutil.copyfile(self.script_folder+'/parameters.py' , self.target_folder+'/parameters.py')
        shutil.copyfile(self.script_folder+'/transfer.py' , self.target_folder+'/transfer.py')

        print('MXairfoil: refresh the scripts, from main folder to python dictionary')
    def go_env(self):
        # try to install env here.
        print('MXairfoil: it looks not easy to install env here. zhao bao')

if __name__=="__main__":
    zou = refresh()
    zou.go_file()
   



