from operator import index

import pandas as pd

"""
pandas
 1.数据分析库 用于数据处理合分析
 2.基于numpy构建
 3.提供Series[集合] 和 DataFrame [EXCEL表格数据]
 
"""

# 定义一维数据

# 方式1: 分别指定data和index
datas = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(datas['a'])
# 方式2: 使用字典
datas2 = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(datas2['b'])

# 定义多维数据

# 方式1- 先定义数据 再指定column
temp = [
    [1, 'jack', 100],
    [2, 'tom', 80],
    [3, 'root', 90],
]
df1 = pd.DataFrame(temp, columns=('no', 'name', 'score'))
print(df1['no'])

# 方式2-从字典创建
temp2 = {
    'no': [1, 2, 3],
    'name': ['jack', 'tom', 'root'],
    'score': [100, 80, 90]
}
df2 = pd.DataFrame(temp2)
print(df2)

#读取

