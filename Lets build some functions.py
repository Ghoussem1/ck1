# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wGvAQslnNSPItGTi0Mtn_QjRBHI0zxtg
"""

#Question 1
def max_of_two(x,y):
  if x>y:
    return x
  return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(20, 35, 19))

#Question 2

def calculation(a,b):
  addition = a+b
  substraction = a-b
  return addition, substraction
print (calculation(40, 10))

#Question 3

list1 = [1, 2, 3, 4, 5]
total = sum(list1)
print("Sum of all elements in given list: ", total)
def multiplyList(list1) :
    result = 1
    for x in list1:
         result = result * x
    return result
print(multiplyList(list1))
def EvenOddSum(a, n):
    even = 0
    odd = 1
    for i in range(n):
         if i % 2 == 0:
            even += a[i]
            odd *= a[i]
    print ("Even index positions sum ", even)
    print ("nodd index positions mul ", odd)
arr = list1
n = len(arr)
EvenOddSum(arr, n)
#Question 4
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))
#Question 5 (Bonus)
import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)