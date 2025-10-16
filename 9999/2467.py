# 2467: 용액

import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

s = 0
e = n-1

result = float("inf")

while s < e:

    sum = arr[s] + arr[e]

    if abs(sum) <= abs(result):
        result = sum

        v1 = arr[s]
        v2 = arr[e]

    if sum > 0:
        e -= 1

    else:
        s += 1

print(v1, v2)