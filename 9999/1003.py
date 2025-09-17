# 1003: 피보나치 함수

# 각 fibonacci(n)에 대해 fibonacci(0) 과 fibonacci(1)이 호출된 횟수

import sys

def tupleSum(x,y):
    return (x[0] + y[0], x[1] + y[1])

def printed(n):

    memo = {}
    memo[0] = (1,0)
    memo[1] = (0,1)

    for i in range(2, n + 1):
        memo[i] = tupleSum(memo[i-1], memo[i-2])

    return memo[n]

n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    for item in printed(x):
        print(item, end = " ")
    print()

    