# 12865: 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().split()) # N 물품 수 K 최대 무게

item_arr = []
dp = [[0 for _ in range(N + 1)] for _ in range(K+1)] # dp[i][j]는 최대 무게 i 일때 j 번째 아이템까지 사용할시 최대 value

for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    item_arr.append((W, V))

# base case: 최대 무게가 0 일때 최대 value 또한 0, 아이템을 아무것도 사용하지 않을때 또한 0

for i in range(1, K+1):
    for j in range(1, N+1):

        dp[i][j] = dp[i][j-1]

        if item_arr[j-1][0] <= i:
            dp[i][j] = max(dp[i][j], dp[i-item_arr[j-1][0]][j-1] + item_arr[j-1][1])

print(dp[K][N])
