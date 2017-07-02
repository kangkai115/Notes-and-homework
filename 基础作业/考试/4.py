import time
import os
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args)
        print('end time: %s'%(time.strftime('%x',time.localtime())) )
        t1=time.time() - t0
        print('run time: %s'%t1)
        t1='运行时间为'+str(t1)+'''
'''
        with open('1.txt','a') as f:
            f.write('%s'%func.__name__+t1)
            return back
    return new_fun


@run_time
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
    
@run_time
def fab_yield(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L
##    n, a, b = 0, 0, 1
##    while n < max:
##        yield b
##        print(b)
##        a, b = b, a + b
##        n = n + 1
##L = [i for i in fab_yield(max)]
####    print(L)
