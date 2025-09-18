# 9095: 1,2,3 더하기

"""정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오."""

import sys

def oneTwoThree(n):

    dp =[0 for _ in range(max(4,n + 1))]

    # base case
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    

    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp [i-1] 

    return dp[n]

n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())
    print(oneTwoThree(k))
