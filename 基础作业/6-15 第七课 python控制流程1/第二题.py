while 1:
    a=input('输入一个不多于5位的正整数：')
    if a=='q':
        break
    elif len(a)>5:
        print('您输入的数字大于5位,请重新输入，如要退出请输入q')
    else:
        print('您输入的数字是%d位'%len(a))
        b=[]
        c=len(a)
        while c:
            b.append(str(int(a)%10))
            a=int(a)/10
            c-=1
        print('该数字的倒叙是：%s'%(''.join(b)))
        break
