#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

x = np.array([0, 1])  # 入力
w = np.array([0.5, 0.5])  # 重み
b = -0.7  # バイアス
print(w*x)  # array([ 0. , 0.5])
print(np.sum(w*x))  # 0 + 0.5 = 0.5
print(np.sum(w*x) + b) # (およそ-0.2)
