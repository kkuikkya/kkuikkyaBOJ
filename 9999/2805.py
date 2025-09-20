#2805: 나무 자르기

import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
           
s = 0
e = max(arr)

while s <= e:

    mid = (s + e) // 2

    total = 0

    for x in arr:
        if x > mid:
            total += x - mid

    if total >= M:
        result = mid
        s = mid + 1

    else:
        e = mid - 1

print(result)
