# 1463: 1로 만들기

"""정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

import sys

def make1(n):

    # base case:
    if n == 1:
        return 0

    case2 = case3 = float("inf")
    
    case1 = 1 + make1(n-1)
    
    if n % 2 == 0:
        case2 = 1+ make1(n / 2)

    if n % 3 == 0:
        case3 = 1 + make1(n / 3)

    return min(case1, case2, case3)

def make1DP(n):
    dp = [float("inf") for _ in range(n + 1)]

    dp[1] = 0
    # base case dp[1] = 0

    for i in range(2, n+1):
        
        # 2를 나누는 경우
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1

        # 3을 나누는 경우
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1

        # 1을 빼는 경우
        if dp[i-1] + 1 < dp[i]:
            dp[i] = dp[i-1] + 1

    return dp[n]


n = int(sys.stdin.readline())

print(make1DP(n))