#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:56:17 2018

This problem defines the longest Collatz-Chain

@author: sam
"""

n = 13

while n >= 0:
    if n%2 == 0:
        new = n/2
    else:
        new = 3*n - 1

print(n)    
