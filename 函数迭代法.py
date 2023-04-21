# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:36:52 2023

@author: 86319
"""

def f(x):
    return x ** 3 - x - 1  # 定义方程

def g(x):
    return (x + 1) ** (1 / 3)  # 将方程转化为迭代公式

def fixed_point(p0, tol):
    p = g(p0)  # 计算下一个近似解
    n = 1  # 迭代次数
    while abs(p - p0) > tol:  # 判断是否满足精度要求
        p0 = p  # 更新当前近似解
        p = g(p0)  # 计算下一个近似解
        n += 1  # 更新迭代次数
    return p, n  # 返回近似解和迭代次数

# 设置初始值和容差
p0 = 1.0
tol = 0.00001

# 调用函数求解
root, n_iter = fixed_point(p0, tol)

# 输出结果
print(f"迭代 {n_iter} 次后，得到的近似根为：{root:.6f}")