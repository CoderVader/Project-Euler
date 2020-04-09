#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 00:49:33 2018

Description: This program reads an external txt file
and sorts its contents 

@author: sam
"""

file = open("names.txt", 'r')
names = file.readlines()
names.sort()
print(names)