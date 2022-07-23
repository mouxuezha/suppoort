# this is to analyze the time cost of different part

import time
from functools import wraps

class time_ratio(object):

    def __init__(self,zhonglei_list = ['train_ANN','surrogate']) -> None:
        self.jishi_dic = {'all':0}
        self.start_dic = {'all':0}
        self.zhonglei_list = zhonglei_list
        self.clear_all()
        self.all_start()
        pass

    def all_start(self):
        self.total_time_start = time.time()
        for zhonglei in self.zhonglei_list:
            self.jishi_dic[zhonglei] = 0
            self.start_dic[zhonglei] = self.total_time_start

    def jishi_type_start(self, zhonglei):
        if zhonglei in self.jishi_dic:
            self.start_dic[zhonglei] = time.time()
        else:
            raise Exception('MXairfoil: undefined type in time_ratio')
            
    def jishi_type_end(self,zhonglei):
        if zhonglei in self.jishi_dic:
            if self.start_dic[zhonglei] ==0 :
                raise Exception('MXairfoil: end a jishi before start, G!')
            self.jishi_dic[zhonglei] = self.jishi_dic[zhonglei] + time.time() - self.start_dic[zhonglei]
            self.start_dic[zhonglei] = 0 
        else:
            raise Exception('MXairfoil: undefined type in time_ratio')

    def jishi_type_decorate(self,zhonglei,func):
        @wraps(func)
        def func_return(*args,**kargs):
            self.jishi_type_start(zhonglei)
            jieguo = func(*args,**kargs)
            self.jishi_type_end(zhonglei)
            return jieguo
        print('MXairfoil: function decorated by time_ratio.')
        return func_return

    def get_result(self,model='str'):
        rizhi = 'MXairfoil: get result from time_ratio: '
        total_time = time.time() - self.total_time_start
        rizhi = rizhi + '\ntotal time cost: ' + str(total_time)
        bili = [] 
        for zhonglei in self.zhonglei_list:
            zhonglei_time = self.jishi_dic[zhonglei]
            zhonglei_time_bili = zhonglei_time / total_time
            bili.append(zhonglei_time_bili)
            rizhi = rizhi + '\n'+zhonglei+' time cost: ' + str(zhonglei_time) + '  bili : '+str(zhonglei_time_bili*100) + '%'

        if model=='str':
            print(rizhi)
            return rizhi 
        else:
            return bili

    def clear_all(self):
        for zhonglei in self.zhonglei_list:
            self.jishi_dic[zhonglei] = 0
            self.start_dic[zhonglei] = 0        

class time_ratio_debug(time_ratio):
    def __init__(self) -> None:
        self.shishi = time_ratio(zhonglei_list = ['train_ANN','surrogate','shishi'])
        pass
    
    def yimiao(self):
        time.sleep(1)
        print('MXairfoil: -1s   -@..@-')

    def banmiao(self):
        time.sleep(0.5)
        print('MXairfoil: 0.5* -1s')
    
    def liangmiao(self):
        time.sleep(1) 
        print('MXairfoil: -1s, -@..@-')
        time.sleep(1) 
        print('MXairfoil: -1s. -@..@-')

    def time_ratio_test(self):
        n=2
        self.shishi.all_start() 
        self.shishi.jishi_type_decorate('shishi',self.liangmiao)()
        # self.liangmiao()
        for i in range(n):
            # self.shishi.jishi_type_start('train_ANN')
            # self.yimiao()
            # self.shishi.jishi_type_end('train_ANN')
            self.shishi.jishi_type_decorate('train_ANN',self.yimiao)()
            
            self.shishi.jishi_type_start('surrogate')
            self.banmiao()
            self.shishi.jishi_type_end('surrogate')
        self.shishi.get_result()

if __name__ == '__main__':
    shishi = time_ratio_debug()
    shishi.time_ratio_test()