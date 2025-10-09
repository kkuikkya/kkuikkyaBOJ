# 9465: 스티커

import sys

def sticker():
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if n == 1:
        return max(arr[0][0], arr[1][0])

    dp = arr # dp[i][j] 는 i행 j열 의 스티커가 선택되었을때의 최대 값

    dp[0][1] = dp[1][0] + dp[0][1] 
    dp[1][1] = dp[0][0] + dp[1][1]

    maxv = max(dp[0][1], dp[1][1])

    for j in range(2, n):
        for i in range(2):

            if i == 0:
                dp[i][j] = max(dp[1][j-1], dp[1][j-2]) + arr[i][j]

            else:
                dp[i][j] = max(dp[0][j-1], dp[0][j-2]) + arr[i][j]

            if dp[i][j] > maxv:
                maxv = dp[i][j]
    
    return maxv

TC = int(sys.stdin.readline())

for _ in range(TC):
    print(sticker())
                

            

