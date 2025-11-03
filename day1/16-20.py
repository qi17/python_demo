"""
16 - 两个字符串排序后是否相等
"""
# s1 = 'abc'
# s2 = 'bca'
# print(sorted(s1) ==sorted(s2))


"""
17 - 统计目录下的文件大小
"""
import os
# print(os.listdir("../day1"))
# sum_size = 0
# for file in os.listdir("../day1"):
#     if os.path.isfile('../day1/'+file):
#         sum_size += os.path.getsize('../day1/'+file)
#
# print(sum_size)



"""
18 - 反转字符串
"""
# s = input("请输入一个字符串")
# print(s)
# # 切片 反转
# print(s[::-1])

"""
19 - 合并目录下的所有文本
"""

# dir_path = "./txt"
# output_file = './txt/merged.txt'
# # 先打开写入的合并文件
# with open(output_file, 'w', encoding='utf-8') as outfile:
#     # 遍历目标路径文件
#     for fileName in os.listdir(dir_path):
#         if fileName.endswith('.txt'):
#             # join 拼接路径
#             with open(os.path.join(dir_path,fileName),'r') as f:
#                 outfile.write(f.read())

"""
20 - 合并目录下的所有文本
"""

li = [1,2,3,4,5]
# 列表推导式
res =[ x for x in map(lambda  x: x**2,li) if x>10]
print(res)