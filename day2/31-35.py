"""
31 - 提取电子邮箱
"""
import re
patter_email =r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'
i = input("请输入字符串:")
s= re.compile(patter_email,re.S)
print(re.findall(s,i))


"""
32 - 密码校验
"""
import re
def check_pwd(pwd):
    if not 6<= len(pwd) <=20:
        return False,"密码长度必须是6-20"
    if not re.findall(r'[a-z]',pwd):
        return False,"必须包含一个小写字母"
    if not re.findall(r'[A-Z]', pwd):
        return False, "必须包含一个大写字母"
    return True
print(check_pwd("1456aA23"))



"""
33 - 提取商品价格信息
"""
import re
s ="小S上街买菜，买了3斤黄瓜花了9元;买了4斤苹果花了13元;买了5斤西瓜花了5元"
for str in s.split(';'):
    result = re.search(r'买了(\d)斤(.*)花了(\d+)元',str)
    print(result.groups())


"""
34 -字符串拼接
"""
# str =['hello','world','yoyo']
# print("_".join(str))


"""
35 - 统计字符串出现的次数
字符串忽略大小写 casefold() 
"""

s = 'Hello,welcome to my world'
word = input("请输入一个字符")
num = 0
for i in s:
    if word.casefold() == i.casefold():
        num += 1
if num == 0:
    print("没有这个字符")
else:
    print("字符:%s" % word + "出现了%d" % num + "次")
