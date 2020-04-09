#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 01:11:24 2018

@author: sam
"""

num = 0
add = 0
for num in range(1,100000):
   if num > 1:
        for i in range(2,num):
          if num%i == 0:
                break
        else:
           add += num
print(add)           
          
