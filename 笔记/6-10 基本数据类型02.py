#列表
li = [2,3,4,5,6]

#字符串
f = '人生苦短，我用python'
b = 'this is string test'
b.count('t')#计算b中t的个数
b.endswith('t')#查看b中最后一个元素是否为t,是则True，不是则False
b.startswith('e')#查看b中第一个元素是否为e,是则True，不是则False
#python3中用的是utf-8
b.find('i')#查找b中第一个i的位置，如果有则返回位置，如果没有返回-1
b.find('a',2,10)#查找b中第一个i的位置（从2到10个元素中查找），如果有则返回位置，如果没有返回-1
b.index('i')
#b.index('a')查找b中第一个a的位置，如果有则返回位置，如果没有报错
c = 'abcdefg'
c.isalpha() #判断字符串是不是都是字符组成
d = '123456'
d.isdigit() #判断字符串是不是都是数字组成
c.upper() #字符转成大写
#列表可变序列，字符串和元组是不可变序列
c = 'ABCDEFG '
c.lower() #字符转成小写
c.islower()#查看c是否都为小写
b = 'aaaaa'
b.replace('a','b')#将a全部替换为b
b.replace('a','b',1)#将第一个a替换为b
b = 'this is string test'
b.split()#会将b编程一个list因为没有分割条件
b.split('i')#将b编程一个list，以i分割
b.split('i',1)#将b编程一个list，以i分割，只分割第一个i

#字符串的拼接
s = 'hello'
t = 'python'
r = '!'
#1
s + t +r
s + ' ' + t + ' ' + r
#2  格式化字符串  %s
'%s %s %s'%(s,t,r)
#3 join
' '.join([s,t,r])#重要！！！！！！！！可以把list中的元素输出成str list中都要为字符串 ‘’join(list) 
#4 format
'{} {} {}'.format(s,t,r)
'{0} {1} {2}'.format(s,t,r)
'{2} {1} {0}'.format(s,t,r)
'{n0} {n1} {n2}'.format(n2=s,n0=t,n1=r)

#格式化
'%d'%123 #格式化整型
'%.2f'%2.3 #格式化小数
'%3.2f'%2.3
'%c'%97  #格式化ASCII字符
'%o'%8 #格式化为8进制
'%o'%7
'%x'%16
'%x'%10#格式化为16进制
'%e'%10.23
'%e'%0.023#格式化为科学计数法

#  '%m.nf'  m 表示长度  n 表示小数位数
'%-7.2f'%2.3 #左对齐  
'%07.2f'%2.3 #用0填充
'%-07.2f'%2.3
'%+7.2f'%2.3 #正数前面添加+
'%0+7.2f'%2.3
'%-+7.2f'%2.3

'%5s'%'ab'
'%-5s'%'ab'

#转义
e = """python
"""
"""
\ 是转义符
\n  换行
\a  提示音
\t  tab  横向制表符
\b  退格符
\r  回车键
\f  换页

"""
print('\a')
print('xyz\tmn')
print('xyz\bmn')
print('xyz\rmn')
print('xyz\fmn')

g = 'abcd\'bgfg\'efg'
h = "abdf'agg'agagf"














