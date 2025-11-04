"""
21 - 句子大写
"""
import math

words = "hello world hello kira"
print(words.upper())

"""
22 - 计算字母和数字的程序
"""

s = input("请输入一个字符串")
s_count =0
n_count =0

for char in s :
    if char.isalpha():
        s_count+=1
    else:
        n_count+=1

print("您输入字母个数:",s_count)
print("您输入数字个数:",n_count)


"""
23 - 替换空格
"""
s = input("请输入一个字符串")
print(s.replace(" ",''))


"""
24 - 使用列表推导式输出每个奇数
"""

result = [i for i in range(1,101) if i % 2 ==0 ]
print(result)

"""
25 - 定义类计算圆的面积
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area())
