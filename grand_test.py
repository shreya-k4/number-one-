# -*- coding: utf-8 -*-
"""grand test

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hz4nWMkSHvGiNR_8UAr8B4wkls5iFtGA
"""

n=  int(input())
sum1 = 0
for i in range(1,n):
  if (n % i == 0):
     sum1 =sum1 + i 
if (sum1 == n):
  print("the number is a perfect number ")
else:
  print("the number is not a perfect number ")

6