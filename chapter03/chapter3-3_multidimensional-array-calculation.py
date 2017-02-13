#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

## 一次元配列.
print("一次元配列:")
A = np.array([1, 2, 3, 4])
print(A)

## 配列の次元数を求める
print(np.ndim(A))

## 配列の形状を求める
print(A.shape)

print(A.shape[0])

## 二次元配列.
print("二次元配列:")
B = np.array([ [1,2], [3,4], [5,6] ])
print(B)
## 配列の次元数を求める
print(np.ndim(B))
## 配列の形状を求める
print(B.shape)

## 3.3.2 行列の内積
print("行列の内積")
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])
print(A.shape)
print(B.shape)
print(np.dot(A,B))

A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])
print(np.dot(A,B))

## 3.3.3 ニューラルネットワークの内積
print("ニューラルネットワークの内積")
X = np.array([1,2])
print(X.shape)
W = np.array([[1,3,5], [2,4,6]])
print(W)
print(W.shape)
print(np.dot(X,W))