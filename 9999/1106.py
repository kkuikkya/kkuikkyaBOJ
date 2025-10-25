# 1106: 호텔

import sys

C, N = map(int, sys.stdin.readline().split())
ways = []

for i in range(N):
    cost, custumer = map(int, sys.stdin.readline().split())
    ways.append((cost, custumer))

# DP 테이블 크기를 C + 101 정도로 넉넉하게 잡는다(C값보다 더 큰게 쌀 가능성이 있음)
MAX_C = C + 101 

# dp[j] = 정확히 j명을 모으는 최소 비용
dp = [float('inf')] * (MAX_C)


# base case: 0명을 모으는 데는 0원
dp[0] = 0

# DP
for cost, custumer in ways:
    # 이 '방법'을 사용해서 갱신할 수 있는 모든 j를 순방향으로 순회

    for j in range(custumer, MAX_C):

        # j명을 모으는 기존 비용(dp[j])과 j - custumer 에서 이번 방법을 추가하는 것 중 최소값을 선택
        if dp[j - custumer] != float('inf'): # 이전 상태가 도달 가능해야 함
            dp[j] = min(dp[j], dp[j - custumer] + cost)


# 적어도 C명이므로 C보다 큰 값중에 최소값을 반환
print(min(dp[C:]))