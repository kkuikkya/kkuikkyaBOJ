# 1562: 계단 수

# 뒤지게 어렵네.. ㅋㅋ

import sys
MOD = 1000000000

def solve():
    n = int(sys.stdin.readline())

    dp = [[[0] * (1<<10) for _ in range(10)] for _ in range(n + 1)] 
    # dp[i][j][bitmask] 는 길이 i 와 끝나는 숫자 j 이고 [bitmask] 만큼 채워져 있는 수의 개수

    # base case, 0으로 시작하는 경우는 없음
    for i in range(1, 10):
        dp[1][i][(1 << i)] = 1

    for i in range(2, n+1):
        for j in range(10):
            for bitmask in range(1 << 10):
                newmask = bitmask | (1 << j)

                # case1: 9로 끝나는 경우
                if j == 9:
                    dp[i][j][newmask] = (dp[i][j][newmask] + dp[i-1][j-1][bitmask]) % MOD

                # case2: 0으로 끝나는 경우
                elif j == 0:
                    dp[i][j][newmask] = (dp[i][j][newmask] + dp[i-1][j+1][bitmask]) % MOD

                # case3: 그 외 앞 뒤올 하나씩 추가 가능
                else:
                    dp[i][j][newmask] = (dp[i][j][newmask] + dp[i-1][j-1][bitmask]) % MOD
                    dp[i][j][newmask] = (dp[i][j][newmask] + dp[i-1][j+1][bitmask]) % MOD

    total = 0
    for j in range(10):
        total = (total + dp[n][j][(1<<10) -1]) % MOD # 길이는 n이고 비트마스크가 모두 채워져 있는 개수
    return total

print(solve())