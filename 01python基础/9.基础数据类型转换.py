# 数据类型转换

# 数据类型总结
'''
字符串 string
数字类型 Number
    整型 int
    浮点 float
    复数
    布尔 bool
列表  list
元组  tuple
字典  dict
集合  set

可变数据类型：列表，字典，集合
不可不数据类型： 字符串，数字，元组

容器类型数据 ： 字符串，列表，元组，集合，字典
非容器类型数据： 数字，布尔类型
'''


# 数据类型转换
'''
什么是数据类型转换？
    把一个数据类型转换为另一个数据类型，例如 字符串转为数字
为什么需要数据类型转换？
    因为不同的数据类型之间不能运算
数据类型转换的形式？
    自动类型转换
    强制类型转换
'''

# 自动类型转换
# 当两个不同的值进行运算时，结果会向更高的精度进行计算
# True ==> 整型 ==> 浮点 ==> 复数
a = 123
b = True  # 在和数字运算时 True转为数字1，False转为数字 0
# print(a+b)
# print(12.5+22)
# print(True+3.14)

'''
if 表达式：
    真区间
else：
    假区间
'''
# if a:
#     print('真')
# else:
#     print('假')


# 强制类型转换
'''
下面的函数，可以把其它类型的数据，转换为对应的数据类型
str()  
int()
float()
bool()
list()
tuple()
dict()
set()
'''
a = 'love'
# a = '123'
# a = '123.5'
# a = '123abc'
# a = 123
# a = 3.14
# a = True
# a = [1,2,3]
# a = (22,33)
# a = {11,22}
# a = {'a':1,'b':2}
print(a,type(a))

#  str() 可以把所有的其它数据类型转换为字符串类型
# res = str(a)
# 字符串转数字类型时，如果字符串中时纯数字，可以转换
# 其它容器类型不能转为数字int类型
# res = int(a)
# 浮点类型的转换和int类型一样，不过转换的结果是浮点类型
# res = float(a)
# bool可以把其它类型转换布尔类型的True或False
# 需要总结，哪些情况转bool的结果是 False
'''
    '0' True
    '' False
     0
     0.0
     False
     []
     {}
     ()
     set()
'''
# res = bool(a)

#
# print(res,type(res))
