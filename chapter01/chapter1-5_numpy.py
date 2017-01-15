#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

## 1.5.2 Numpy配列の生成
print("## 1.5.2")
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

## 1.5.3 Numpyの算術計算
print("## 1.5.3")
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x * y) # element-wise product
print(x / y)
print(x / 2.0) # broadcast

## 1.5.4 NumpyのN次元配列
print("## 1.5.4")
##A = np.array([[1,2], [3.4]])
##配列間に空行を入れると認識してくれなくなった。そういうものなのか...
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3,0],[0,6]])
print A+B

print A+10

## 1.5.5 ブロードキャスト
print("## 1.5.5")
AA = np.array([[5,6],[7,8]])
BB = np.array([10,20])
print AA+BB

## 1.5.6 要素へのアクセス
print("## 1.5.6")
X = np.array([[51,55],[14,19],[0,41]])
print(X)
print(X[2])
print(X[1][1])

for row in X:
    print(row)

## Xを一次元配列へ変換
print X.flatten()
print X.flatten()[np.array([0,2,4])]
print X.flatten() > 15