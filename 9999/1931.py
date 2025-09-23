# 1931: 회의실 배정

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))

result = []
last = 0

for item in arr:
    
    if item[0] >= last:
        result.append(item)
        last = item[1]

print(len(result))

    