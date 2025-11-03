"""
1-两数之和
"""
import math

t1 = float(input("请输入第一个数字："))
t2 = float(input("请输入第二个数字："))
sum = t1 + t2
print("两数之和:", t1, "+", t2, "=", sum)


"""
2-阶层
"""
count = 1
for i in range(1, 6):
    count *= i
print(count)


"""
3-求素数
"""
def se(start, end):
    result = []
    for i in range(start, end):
        if is_prime(i):
            result.append(i)
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(se(1, 10))


"""
4-求n个数字的平方和
"""
def sum_square(n):
    # sum =0
    # for i in range(1, n):
    #     sum+= n*n
    # return sum
    return n * (n+1) * (2*n+1)/6
print(sum_square(3))

"""
5-计算圆的面积
"""
def circle_area(r):
    ## ** 可以表示幂 比如平方 立方 分别是 **2 **3
    return math.pi * r ** 2
print(circle_area(2))
