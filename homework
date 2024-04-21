#Задание 3

import matplotlib.path as mplPath

# 多边形的顶点
polygon = [(3, 1), (1, 3), (-1, 1), (-2, -3), (1, -4), (3, -2)]
path = mplPath.Path(polygon)

# 需要检查的点
points = [(1, -1), (-1, 2)]

# 检查每个点是否在多边形内
for point in points:
    inside = path.contains_point(point)
    print(f"点 {point} {'在多边形内' if inside else '不在多边形内'}")


#Задание 4
import matplotlib.path as mplPath

# 多边形的顶点
polygon = [(3, 1), (1, 3), (-1, 1), (-2, -3), (1, -4), (3, -2)]
path = mplPath.Path(polygon)

# 需要检查的点
points = [(1, -1), (-1, 2)]

# 检查每个点是否在多边形内
for point in points:
    inside = path.contains_point(point)
    print(f"点 {point} {'在多边形内' if inside else '不在多边形内'}")

#Задание 4  12.11（1）

import numpy as np

# Векторы g и h
g1 = np.array([1, 2, 3])
g2 = np.array([0, 2, 3])
g3 = np.array([0, 1, 2])
h1 = np.array([0, 9, 10])
h2 = np.array([-1, 12, 8])
h3 = np.array([0, 8, 5])

# Матрица G составленная из векторов g
G = np.column_stack((g1, g2, g3))

# Матрица H составленная из векторов h
H = np.column_stack((h1, h2, h3))

# Находим матрицу линейного оператора
A = np.linalg.inv(G).dot(H)

print("Матрица линейного оператора A:")
print(A)
#12.11（2）
# Векторы g и h для второй системы
g1 = np.array([2, 0, 1])
g2 = np.array([0, -1, 2])
g3 = np.array([2, 1, 3])
h1 = np.array([3, -1, 2])
h2 = np.array([1, -3, 1])
h3 = np.array([6, -2, 1])

# Матрица G и H для второй системы
G = np.column_stack((g1, g2, g3))
H = np.column_stack((h1, h2, h3))

# Находим матрицу линейного оператора для второй системы
A = np.linalg.inv(G).dot(H)

print("Матрица линейного оператора A для второй системы:")
print(A)
#12.12
import numpy as np

# 平面 π 的法向量
normal_vector = np.array([1, -2, 1])

# 单位矩阵，代表在 V2(π) 上的恒等操作
identity_matrix = np.eye(3)

# 将法向量乘以2
transformed_normal_vector = 2 * normal_vector

# 构建算子的矩阵
# 因为在 V2(π) 上是恒等操作，所以只需要修改法向量对应的列
operator_matrix = identity_matrix
operator_matrix[:, 2] = transformed_normal_vector

print("线性算子的矩阵:")
print(operator_matrix)
#12.13
import nump
