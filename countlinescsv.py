# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:27:05 2017

@author: dimitri.cabaud
"""
import mmap

def mapcount(filename):
    with open(filename, "r+") as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
    return lines

print(mapcount("Output.csv"))
