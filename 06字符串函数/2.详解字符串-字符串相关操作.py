# 字符串相关操作

# - 字符串 + 操作
vara = '君不见，黄河之水天上来，奔流到海不复回.'
varb = '君不见，高堂明镜悲白发，朝如青丝暮成雪'
# res = vara + varb
res = '将进酒 '+'李白'
# print(res)

# - 字符串 * 操作
# vars = '鸡你太美,' * 5
# print(vars)
# 鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美

# - 字符串 [] 切片操作 ****
# 字符串的索引操作，字符串中只能使用[]下标 访问，不能修改
'''
0 1 2 3 4 5 6 7 8 9 10 ....
君不见，黄河之水天上来，奔流到海不复回
                    -4 -3 -2 -1
'''
vars = '君不见，黄河之水天上来，奔流到海不复回'
# print(vars[5])
# print(vars[-5])

'''
字符串的切片操作
str[开始值：结束值：步进值]
开始值：默认为0，结束值默认是最后一个下标，步进值默认为1
'''
# print(vars)
# print(vars[5]) # 写一个值就是获取指定下标的元素
# print(vars[2:5]) # 从2下标开始取值，一直到下标5之前，能取到2，取不到5
# print(vars[4:8:2]) # 黄河之水 ==> 黄之
# print(vars[::]) # 从头取到尾
# print(vars[::2]) # 从头取到尾，每隔一个取一个
# print(vars[::-1])  # 字符串倒转过来
# print(vars[::-2])  # 字符串倒转过来，每隔一个取一个
# print(vars[1::])  # 不见，黄河之水天上来，奔流到海不复回
# print(vars[1::2])  # 不，河水上，流海复



