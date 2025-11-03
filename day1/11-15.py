"""
12-读取文件并排序
"""
from random import Random

# def read_file():
#     lines = []
#
#     with open('students.txt', 'r',encoding= 'utf-8') as file:
#         while True:
#             line = file.readline()
#             if len(line) == 0:
#                 break
#             lines.append((int)(line.split(",")[2].strip()))
#         return lines
# print(sorted(read_file()))
# print(sum(read_file()))

"""
13-读取文件获取最高分和最低分
"""
# def read_file():
#     lines = []
#     with open('students.txt', 'r', encoding='utf-8') as f:
#         while True:
#             line = f.readline()
#             if len(line) == 0:
#                 break
#             lines.append((float)(line.split(",")[-1].strip()))
#     return lines
#
#
# lines = read_file()
# lines.sort()
# print(lines)
# min_score = min(lines)
# max_score = max(lines)
# print("最低分:%s" % (lines[0]) + ";" + "最高分:%s" % (lines[-1]))
# print("最低分:%s" % (min_score) + ";" + "最高分:%s" % (max_score))

"""
14-统计出现次数最多的单词
"""
# def read_file():
#     result = {}
#     with open('words.txt', 'r', encoding='utf-8') as f:
#         # 逐行读取
#         for line in f:
#             # 去除行尾换行符，然后按空格分割
#             words = line.strip().split(" ")
#
#             for word in words:
#                 if word:  # 确保不是空字符串
#                     if word not in result:
#                         result[word] = 0
#                     result[word] += 1
#     return result
# result = read_file()
# print(result)
# from collections import Counter
# count= Counter(result)
# print(count.most_common(1))
# print(sorted(result.items(),key=lambda  x: x[1],reverse=True))

"""
15 - 猜数字
"""
import random
def guess_num():
    num = random.randint(1,10)
    while True:
        guess = int(input("请输入一个数字:"))
        if guess == num:
            print("你猜对了")
            break
        elif guess < num:
            print("你输入的数字小了")
        else:
            print("你输入的数字大了")

guess_num()