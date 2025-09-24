# 11404: 플로이드

import sys
from collections import defaultdict

n = int(sys.stdin.readline()) # vertex

m = int(sys.stdin.readline()) # edges

memo = [[float("inf") for _ in range(n)] for _ in range(n)] # memo[i][j] 는 i 에서 j 까지 가는 최소 거리


for _ in range(m):
    
    u, v, weight = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1

    if memo[u][v] > weight: 
        memo[u][v] = weight

for i in range(n):
    memo[i][i] = 0
    
# Floyd
for k in range(n):
    for i in range(n):
        for j in range(n):
            
            if memo[i][j] > memo[i][k] + memo[k][j]:
                memo[i][j] = memo[i][k] + memo[k][j]


for i in range(n):
    for j in range(n):
        # 만약 경로가 없어서 inf 라면 0을 출력
        if memo[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(memo[i][j], end=" ")
    print() # 줄바꿈