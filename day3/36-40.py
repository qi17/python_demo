"""
36 - 字符串不是纯数字
"""
# s = 1.2
# try:
#     if s.isdigit():
#         print(s+"是纯数字")
#     else:
#         print(s + "不是纯数字")
# except Exception as e:
#     print(e)


"""
37 - 将字符串 s ='ajkjdlajkfaikudda'去重再排序
"""
# s = 'ajkjdlajkfaikudda'
#
# se = set(s)
# print(se)
# print(sorted(se))


"""
38 - 判断对称数组

切片语法 [start:stop:step] :省略-表示从头开始
"""
# li = [1,2,3,3,2,1]
# rev = list(reversed(li))
# # 切片
# slice1 = li[::-1]
# print(li)
# # if li == rev:
# if li == slice1:
#     print("True")
# else:
#     print('False')

"""
39 - 求列表长度最长的

"""
a = ["hello","world","yoyo","congratulations"]
dict = {}
for x in a:
    dict[x] = len(x)
# 返回最大value的key
max_key = max(dict,key = dict.get)
print(max_key)
# 返回最大的key
print(max(dict))
# 返回最大的value
print(max(dict.values()))


"""
40 - 取列表最大的三个值
一个:表示[start:stop] 两个:表示[start:stop:step]
[:1]    → [start:stop]       → start省略，stop=1
[::1]   → [start:stop:step]  → start省略，stop省略，step=1
[:-1]   → [start:stop]       → start省略，stop=-1
[::-1]  → [start:stop:step]  → start省略，stop省略，step=-1

所以一个切片 我们要先判断步长是否为负 
省略位置	当step为正数时	当step为负数时
start	0	            -1 (最后一个元素)
stop	len(序列)	    -len(序列)-1 (开头之前)
step	1	            -1

"""
li = [123,235,99,88,567,1,2,3,100]

print(sorted(li,reverse=True)[:3])

str ='abcdefghij'
print(str[1:-1])


