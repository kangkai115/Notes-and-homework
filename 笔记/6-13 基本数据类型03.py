#字符串 格式化 转义符
a = 'aaa'
'%s'%(a)
'%r'%(a)

# 元组   集合  字典
tu = (1,2,3,12,3)
t1 = 1,2,3,1,1,2,3
t2 = 'a','b','c'

tu.count(1)
tu.index(1)

#元组和列表的嵌套
li = [1,2,3,3,4,5,5,6,5,7,1,2,9]
tu = ('a','b','c')

ls = ['a',li]
l2 = ['b',tu]
t1 = ('c',li) 
t2 = ('d',tu)

'asdf{}dcd'.format(li)
ls[1][3]
l2[1][0]
t1[1]
t1[1][4]

#深复制 和 浅复制
#浅复制
cols = ls.copy()
li[0] = 'a'
id(ls),id(cols)
id(li),id(ls[1]),id(cols[1])

#深复制
import copy
a = copy.deepcopy(ls)
li[0] = 'b'
id(ls) , id(a)

#浅复制对于列表只复制啦引用，没有新建对象

#深复制对于列表复制一个新的对象

#浅赋值   copy  切片  赋值

#保留改变的数据


#集合
se = {1,2,3,3,3,'a','b','c',tu}
sa =  set(['e','f','g'])
s2 = set(tu)
    

"""
特点：
1.无序
2.元素不重复
"""

# 交集  并集  差集

se & s2  #交集   se.intersection(s2)
se - s2  #差集   se.difference(s2)  se.difference_update(s2)
se | sa  #并集   se.union(sa)

se.add('ab')
cose = se.copy()

#se.discard(1)
cose.add('f')
se.issubset(cose)  # 判断se是不是cose的子集
se.issuperset (s2) # 判断s2是不是se的一个子集
#se.pop()
#se.remove(2)
#se.symmetric_difference(s2)
se.update(sa)

#集合基本了解就行，一般来说用不到


#####字典
#键 key   键值
di = {'a':1,'b':2,'a':4}
da = dict(c=3,d=4)

"""
键 唯一  只能不可变对象做键
键值 可以改变
无序
"""

#查看键值
di['a']
#di['a'] = 2
di['c'] = 3  #更新  和 添加

di.fromkeys('abc')
di.fromkeys('abc',10)

di.get('a')
di.get(1,10)
a,b = di.get(1,(1,2))  ##常用

di.items()          ## 键 和 键值
list(di.items())
di.keys()           # 键
list(di.keys())
list(di)            #键值
di.values()
list(di.values())

#di.pop('a')
#di.pop('a',4)
#di.popitem()


di.setdefault(1)
di.setdefault(2,20)

di.update({1:10})
di.update({3:30})

#总结
"""
掌握的
字典
get   keys   values

"""

"""
可变对象 ：  list  dict  set
不可变对象： str  tuple  number
"""










