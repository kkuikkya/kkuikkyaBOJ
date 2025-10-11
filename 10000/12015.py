# 12015: 가장 긴 증가하는 부분 수열

import sys
import bisect

lis = []

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis.append(arr[0])

for i in range(1, len(arr)):

    if lis[-1] < arr[i]:
        lis.append(arr[i])

    else:
        idx = bisect.bisect_left(lis, arr[i])
        lis[idx] = arr[i]

print(len(lis))

