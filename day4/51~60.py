"""
合并两个list
"""
a= ['x','y','z']
b= [1,2,3]
dic = {}
dic = dict(zip(b,a))
print(dic)


""" 
按age从小到大排序
"""
person = [{'name':'jojo','age':10},
          {'name':'coco','age':8},
          {'name':'xixi','age':9}]

print(sorted(person,key = lambda x :x['age'],reverse=True))



""" 
找出列表中大于0的数字
"""
li = [-1,1,2,3,0]
# 1 - 推导式
# res = [ x for x in li  if x>0]
# 2 - lambda filter
res = list( filter(lambda  x: x >0,li))
print(res)

