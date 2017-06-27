import time
def run_time(func):
    def new_fun(*args,**kwargs):
        t0 = time.time()
        #print('star time: %s'%(time.strftime('%x',time.localtime())) )
        back = func(*args)
        #print('end time: %s'%(time.strftime('%x',time.localtime())) )
        #print('run time: %s'%(time.time() - t0))
        time1=time.time()-t0
        return time1
    return new_fun

@run_time
def test_type():
    for i in range(100000):
        type(i)==type

@run_time
def test_isinstance():
    for i in range(100000):
        isinstance(i,int)

def test():
    te_type=[]
    te_isinstance=[]
    for i in range(100):
        te_type.append(test_type())
    for i in range(100):
        te_isinstance.append(test_isinstance())

    ty_time=avg(te_type)
    is_time=avg(te_isinstance)
    if ty_time<is_time:
        print('type快')
    else:
        print('isinstance快')
def avg(li):
    length=len(li)
    return sum(li)/length









##rep_time=input（'请输入测试次数：'）
##type_=input('请输入要对比的类型（int,float,str）：')
##if type_='int':
##    test=input('请输入对比的整形数字：')
##else type_='float':
##    test=input（'请输入对比的浮点型数字：'）
##else type_='str':
##    test=input('请输入对比的字符型字母：')
##while rep_time>0:
##    @run_time
##    def test1():
##        for i in range(100000):
##            type(test)==type_
