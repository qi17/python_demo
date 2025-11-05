"""
41 - 计算两个 三行三列的矩阵
"""
# x =[[1,2,3],
#     [3,2,1],
#     [2,1,3]]
#
# y =[[2,2,3],
#     [3,3,1],
#     [1,1,2]]
#
# z=[[0,0,0],
#    [0,0,0],
#    [0,0,0]]
# for i in range(3):
#     for j in range(3):
#         z[i][j]=x[i][j]+y[i][j]
#
# for i in z:
#     print(i)

"""
42 - 统计1-100的和
"""
sum = 0
for i in range(101):
    sum += i
print(sum)

"""
43 交换
"""

a = 10
b = 20
a, b = b, a
print(a, b)


"""
44  比较
"""
if a >b:
    print('>')
elif a<b:
    print('<')
else:
    print('=')



"""
45 lambda 创建匿名函数
"""
n = lambda  x,y : x** y

print(n(2,10))


"""
46 随机整数和随机小数
"""
import random
# 随机整数
x = random.randint(1,10)
# uniform随机小数
y = random.uniform(1,10)
print(x,y)

"""
47 位运算 &
"""
print(2&3)

"""
48 位运算 |
"""
print(2|3)


"""
49 位运算 ^
"""
print(2^3)



"""
50 取一个整数的4-7位
"""
i = input("请输入一个整数")
print(i[5:8:1])


