"""
6 - 计算列表的和
"""
# li = [1, 2, 3]
# # total = 0
# # for i in li:
# #     total += i
#
# print(sum(li))


"""
7 - 区间范围内偶数
"""
# def num(n1,n2):
#     result =[]
#     for i in range(n1,n2+1):
#         if i % 2 ==0:
#             result.append(i)
#     return result
# n1 =1
# n2 =10
# print("区间范围【%s~%s】内偶数为:"%(n1,n2),num(n1,n2))


"""
8 - 移除列表的多个元素
"""
# li = [1,2,3,4,5,6,7]
# remove = [1,7]
# for i in remove:
#     # 按照元素值移除
#     li.remove(i)
#     # pop按照索引移除并返回元素
#     # i = li.pop(i)
#     print(i)
# print(li)



"""
9 - 对列表元素去重
"""
# li = [10,20,30,30,20,10]
# print(set(li))


"""
10 - 对简单列表排序 
"""
li = [20,10,30]
# 默认reverse=False 升序
sort_li = sorted(li,reverse=True)
# li.sort会修改原始列表
print(li.sort())
print(li)
print(sort_li)
