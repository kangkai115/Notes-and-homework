#python的基本数据类型
#数值类型
#整型 int  浮点型 float  布尔型 bool 复数 complex
#1 2 3 4
a = 1

b = 3.3

c = True  #True 1
d = False #False 0

e = 1 + 2j  # j  表示虚部

#常用的数值运算符
# + - * / //(向下取整) % **（幂）
#向上取整  作业题 *****
#a = q * b + p
#3 = 1 * 1 + 2
#3 是质数 1 3

#赋值运算符
# =  += -= *= /= 等


#序列类型
#字符串 str 列表 list 元组 tuple
#索引值
#定义序列类型
# ' " """  成对出现
f = '人生苦短  我用python'

# 列表 []
li = [1,2,3,3,4,3,6,5,8,7,5,6,5,7,1,2,1,9,'aa']

#元组 ()
tu = (1,2,3)
t1 = 1,2,3
t2 = (2,)

#变量无类型，对象有类型
#序列类型的通用操作
#索引  序列里面的每一个元素都有自己位置编号 
#索引从0开始
#索引 正向索引 和 反向索引
#len 求序列长度
#序列的切片
# [1,7)  #左闭右开  第7位不取 从1 到7之前的都取出来
f[1:7]
f[:7]  #从0开始到 7
f[1:]  #从1开始到 结束
f[:]   #取全部

#序列的类型转换
#str() list() tuple()

#相加 + +=
#重复 * *=

#检查成员
'y' in f
'y' not in f

#列表的常用操作
#列表的方法都讲，字符串和元组,只讲解常用的

#列表的方法
#tab 自动补全
li.append((1,2,3)) #L.append(object) -> None -- append object to end
l2 = li.copy()     #L.copy() -> list -- a shallow copy of L
li.count(3)     
li.extend([1,2])
li.index(5)
li.index(5,6,10)

l2= [1,4,5,7,2,8,3]
l2.sort(key = int)
l3= ['a','dddd','bb','ccc']
l3.sort(key = len)
#key 按照什么规则去排序


