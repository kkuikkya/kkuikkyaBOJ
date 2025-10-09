# 1932: 정수 삼각형

import sys

def int_triangle():

    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    dp = arr # dp[i][j] 는 i 행 j 열 숫자를 최종으로 선택했을 때의 최대 값
             # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + arr[i][j]

            elif j == i:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]

    return max(dp[n-1])

print(int_triangle())
