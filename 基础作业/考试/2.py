##def ranges(start,stop,step=1.0):
##    if type(start)==type(stop)==type(step)==int or type(start)==type(stop)==type(step)==float:
##        list=[]
##        while stop>start:
##            list.append(start)
##            start+=step
##            print(list)
##        return list
##    else:
##        print('输入有误，请输入数字.')


def float_range(start,stop=None,step=1):
    if isinstance(step,float):
            accuracy=len(str(step).split('.')[1])
    else:
        accuracy=0
    if stop==None:
        i=0
        while i<start:
            i=round(i,accuracy)
            yield i
            i+=step
    else:
        i=start
        while i<stop:
            i=round(i,accuracy)
            yield i
            i+=step 
