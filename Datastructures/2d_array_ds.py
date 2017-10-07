#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hour_glasses = 1 + (len(arr[0]) - 3)
sums = []
i = 0
j = 0

while i < hour_glasses:
    ls1 = arr[i]
    ls2 = arr[i + 1]
    ls3 = arr[i + 2]
    j = 0
    while j < hour_glasses:
        first = j
        middle = j + 1
        third = j + 2
        ls_sum = ls1[first] + ls1[middle] + ls1[third] + ls2[middle] + ls3[first] + ls3[middle] + ls3[third]
        sums.append(ls_sum)
        j += 1
    i += 1

print(max(sums))
