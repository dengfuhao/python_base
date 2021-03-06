# 递归函数
'''
递归函数：
    递归函数就是定义了一个函数，然后在函数内，自己调用了自己这个函数
    递归函数内必须要有结束，不然就会一只调用下去，直到调用的层数越来越多，栈溢出
    递归函数是一层一层的进入，再一层一层的返回，
    例子：
        就像是以前上学一样，你坐在最后面一排，最前面有个漂亮的妹子，你想要要的电话，这时怎么办？
        你去拍一拍前面同学的肩膀，让他帮我问问前面妹子的电话，于是这个同学继续拍一拍前面同学的肩膀
        让他问问前面妹子的电话，之后一直从后向前传递这个信息，一只在重复这个过程，
        直到最后一个通过拍了最前面妹子的肩膀，要到了电话之后一层层的返回到最开始的同学手中

斐波那契数列
    1，1，2，3，5，8，13。。。
实现一个数的阶乘：
    1*2*3*4*5*6*7
'''

# 初步认识 递归函数  3 2 1 0
def digui(num):
    print(num) # 3 2 1 0
    # 检测当前的值是否到了零
    if num > 0:
        # 调用函数本身
        digui(num-1)
    print(num) # 0 1 2 3

digui(3)

'''
解析当前递归函数的执行过程：
digui(3) ==> 3 
    digui(3-1) ==> 2
        digui(2-1) ==> 1
            digui(1-1) ==> 0
            digui(0) ==> 0
        digui(1) ==> 1
    gidui(2) ==>2
digui(3) ==> 3
'''