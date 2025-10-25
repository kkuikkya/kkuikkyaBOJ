# 1806: 부분 합

# Sliding window & Converging

import sys

N, S = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[i] + arr[i])

low = 0
high = 1

min_len = float("inf")

if prefix_sum[N] < S:
    print(0)
    exit()

while high <= N:
    current_sum = prefix_sum[high] - prefix_sum[low]

    if current_sum >= S:
        min_len = min(min_len, high - low)
        low += 1

    else:
        high += 1

print(min_len)


