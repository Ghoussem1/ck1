# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1My6L8NXg2Rtp0iSJyMWVSfjomQUkW9GL
"""

#Question 1

import numpy as np

arr = np.array([1, 2, 3])
print(f'NumPy Array:\n{arr}')

list1 = arr.tolist()
print(f'List: {list1}')

#Question 2

import numpy as np
a=np.arange(9).reshape(3,3)
print("original matrix is :\n",a)
m=np.trace(a)
print("trace of matrix :", m)

#question 3

import numpy as np
x = np.array([[1, 2], [3, 5]])
print("Original array: ")
print(x)
print("Values bigger than 2 =", x[x>2])
print("Their indices are ", np.nonzero(x > 2))

#question 5
import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)