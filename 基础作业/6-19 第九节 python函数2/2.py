##def fun1(list1):
##    list2=list1[:]
##    list3=list1[:]
##    list2.sort()
##    list3.sort(reverse=True)
##    print(list1,list2,list3)
##    if list2==list1:
##        print('up')
##    elif list3==list1:
##        print('down')
##    else:
##        print('None')

##def fun2(*a):
##    a=list(a)
##    a_sort=a[:]
##    a_reverse=a[:]
##    a_sort.sort()
##    a_reverse.sort(reverse=True)
##    if a==a_sort:
##        print('up')
##    elif a==a_reverse:
##        print('down')
##    else:
##        print('None')

def fun3(seq):
    if type(seq) in (str,tuple,list):
        def ord_all(x):
            temp=0
            for i in x:
                temp+=ord(i)
            return temp
        if sorted(seq,key=lambda x:ord_all(str(x)))==list(seq):
            print('up')
        elif list(reversed(sorted(seq,key=lambda x:ord_all(str(x)))))==list(seq):
            print('down')
        else:
            print('None')
