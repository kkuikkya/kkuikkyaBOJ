# 10942: 팰린드롬?

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(N)] for _ in range(N)] # dp[i][j] 는 i가 시작인덱스고 j 가 끝인덱스일때 회문인지 저장

# base case: 시작과 끝이 같은경우 이는 회문입니다
for i in range(0, N):
    dp[i][i] = 1

for length in range(2, N+1): # 회문의 길이
    for i in range(0, N + 1 - length): # 시작 인덱스

        j = i + length - 1
        
        if length == 2: # 얘도 사실상 basecase
            if arr[i] == arr[j]:
                dp[i][j] = 1
                continue
        
        if arr[i] == arr[j]:
            dp[i][j] = dp[i+1][j-1]


TC = int(sys.stdin.readline())

for _ in range(TC):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start - 1][end - 1])