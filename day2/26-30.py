"""
26 - 定义一个可以计算两数之和的函数
"""
def sum(n1,n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        return n1 + n2
    except:
        print("请输入数字")

print(sum('1',2))


"""
27 - 输入字符串的所有排列组合
"""
import itertools
def demo27(s):
    # itertools.permutations(x) 可获取字符串的所有组合
    result = list(itertools.permutations(s))
    for r in result:
        res =  " ".join(r)
        print(res)

print(demo27('abc'))


"""
28 - 输出字符串所有数字
"""
s = input("请输入一个字符串")
res = []
for i in s:
    if i.isdigit():
        res.append(i)

print("字符串中的数字为:","".join(res))


"""
29 - 计算日期相隔的天数
"""
from datetime import  datetime
date1 =input("请输入第一个日期(yyyy-MM-dd)")
date2 =input("请输入第二个日期(yyyy-MM-dd)")

date1 = datetime.strptime(date1, "%Y-%m-%d")
date2 = datetime.strptime(date2, "%Y-%m-%d")

day = date2 - date1
print(day.days)


"""
30 - 手机号脱敏
"""
s = 'hello world15637667788'
import  re
pattern = r'1[3-9]\d{9}'
result = re.sub(pattern,"1***XXXX***",s)
print(result)