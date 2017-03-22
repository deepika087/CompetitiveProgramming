__author__ = 'deepika'

import ctypes

def int32_to_uint32(i):
    return ctypes.c_uint32(i).value

n = int(raw_input())

for i in range(0, n):
    num = int(raw_input())
    num = int32_to_uint32(num)
    print int32_to_uint32(~num)
