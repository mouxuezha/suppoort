# this is to rename all files from a folder, univers.

import os

class rename():
    def __init__(self,location) -> None:
        self.location = location
        pass

    def replace(self,str_old='',str_new=''):
        n=0
        for file in os.listdir(self.location):
            file_name_old = os.path.join(self.location,file)
            if os.path.isfile(file_name_old)==True:
                file_new = file.replace(str_old,str_new)
                file_name_new = os.path.join(self.location,file_new)
                os.rename(file_name_old,file_name_new)
                n=n+1
        print('MXairfoil: '+str(n)+' files renamed. \n' + 'str_old :'+str_old + '\nstr_new :'+str_new)
if __name__ == '__main__':
    # weizhi = r'E:\常用-现役\主线的总备份\主线的文档整合\说法是先写个小的把故事讲圆\又寄了一次艹\保险编辑\我在别人第二次返回的基础上改的\Figures'
    weizhi = r'E:\常用-现役\主线的总备份\主线的文档整合\说法是先写个小的把故事讲圆\又寄了一次艹\保险编辑\我在别人第二次返回的基础上改的\Tables'
    shishi = rename(weizhi)
    shishi.replace(str_old='XUOHA_1_',str_new='')
    shishi.replace(str_old='.png',str_new='.jpg')