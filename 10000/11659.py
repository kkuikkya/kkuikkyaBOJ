# 11659: 구간 합 구하기

"""수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오."""

import sys

n, m = map(int, sys.stdin.readline().split()) # n은 배열 길이, m 은 루프 길이

arr = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = dp[i-1] + arr[i-1]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b] - dp[a-1])