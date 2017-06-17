a = 1
b = 2
a == b
a != b
a > b

li = [1,2]
1 in li
3 in li
3 not in li
id(a)
id(b)
a is b
a is not b

1 == 1 and 2 == 2
1 == 1 and 2 == 3
1 == 1 or 2 == 3
1 == 2 or 2 == 3
not 1==1
not 1 == 2


###控制流程
"""
a = 1
b = 2
if a > b:   #if 后面True才执行
    print('OK',a,b)
elif a < b:
    print('a<b',a,b)
else:    
    pass  #什么都不做
    print('NO',a,b)

"""
"""
a = 201706037
b = (a//1000)%10
if b == 5:
    print('你是11班')
elif b == 6:
    print('你是12班')
else:
    print('自己算吧')

"""
"""
a = input('请输入你的学号：')  # 最后都是字符串
#print(a)
#print(type(a))
a = int(a)
b = (a//1000)%10
if b == 5:
    print('你是11班')
elif b == 6:
    print('你是12班')
else:
    print('自己算吧')

"""
"""
a = input('请输入你的学号：')
if len(a) == 9 and a.isdigit():    #if 嵌套最好不要超过三层
    a = int(a)
    b = (a//1000)%10    # ctrl  + ]
    if b == 5:
        print('你是11班')
    elif b == 6:
        print('你是12班')
    else:
        print('自己算吧')
else:
    print('输入长度或类型错误，请检查！')
"""


#while
"""
while 1:  #死循环  False None [] {}   
    print('True')
"""
"""循环不终止 死循环会消耗计算机的资源，甚至卡死整个系统，导致系统崩溃"""

"""
a = 0
while a < 5:   #终止条件
    print(a)
    a += 1   #自增  成好习惯，写循环尽量先把终止条件写好
"""
"""
while True:
    a = input('请输入你的学号,输入0终止：')
    if a == '0':
        break     #终止  
    if len(a) == 9 and a.isdigit():    #if 嵌套最好不要超过三层
        a = int(a)
        b = (a//1000)%10    # ctrl  + ]
        if b == 5:
            print('你是11班')
        elif b == 6:
            print('你是12班')
        else:
            print('自己算吧')
    else:
        print('输入长度或类型错误，请检查！')   
    
"""
"""
c = 0
while c < 3:
    a = input('请输入你的学号,输入0终止：')
    if a == '0':
        break     #终止  
    if len(a) == 9 and a.isdigit():    #if 嵌套最好不要超过三层
        a = int(a)
        b = (a//1000)%10    # ctrl  + ]
        if b == 5:
            print('你是11班')
        elif b == 6:
            print('你是12班')
        else:
            print('自己算吧')
    else:
        print('输入长度或类型错误，请检查！') 
    c += 1
"""
"""
# continue
a = 0
while a < 5:
    print(a)
    if a == 3:
        print(3)
    else:
        #a += 1
        #continue  #继续  之后代码都不执行，直接跳过，跳过本次循环
        #break      #停止整个循环   不管终止条件
    a += 1
"""
list(range(10))   #range 是个范围  可迭代
list(range(3,10))
list(range(3,10,2))
"""
a = 0
while a <=100:
    if a % 2 != 0:
        print(a,end=' ')
    a += 1
"""
"""
for i in range(101):   #for  迭代  依次去取值
    if i %2 == 0:
        print(i)
"""

"""
li = [1,2,3]
for i in li:
    print(i)
    i = 'a'
    print(i)
"""
"""
b = 'qwe'
for i in b:
    print(i)
"""

c = {1:'a',2:'b'}
for i,j in c.items():
    print(i,j)



















