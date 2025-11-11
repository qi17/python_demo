"""
numpy
 1.科学计算库 处理大规模的数组和矩阵数据以及数学运算
 2.底层是C 因此效率很高
 3.核心 ndarray 矢量化运算 广播机制


 关于矩阵的计算
 矩阵A m x n
 矩阵B n x p

 A x B = np.dot(A,B)
 or   A @ B

手动运算是 A的每行 乘 B的每列

C 的第 i 行第 j 列元素 = A 的第 i 行 与 B 的第 j 列 的点积
C[i,j] = Σ(A[i,k] × B[k,j])，对 k 从 1 到 n 求和

注意矩阵大小！！！ 超级大的float会占用内存导致内存溢出

"""
import  time
import numpy as np

# 1- 创建N*N的矩阵A,B
N = 3
A= [[np.random.randint(0,10) for _ in range(N)]  for _ in range(N)]
B= [[np.random.randint(0,10)  for _ in range(N)]  for _ in range(N)]
# 使用numpy把矩阵转为数组
A_np= np.array(A)
B_np= np.array(B)

# 矩阵的乘法
np_dot = np.dot(A_np, B_np)

# 2-数据文件的读写
# 2.1读写文件类型 如txt csv格式
np.savetxt('array.txt', A_np, delimiter=',')
str = np.loadtxt('array.txt', delimiter=',')
print(str)
# 2.2 读写二进制np格式
np.save('array.npy', str)
np.load('array.npy')

# 3-ndarray类型
# np.array()是一个函数
# np.ndarray是一个类型

