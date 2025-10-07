# 1629: 곱셈

import sys

A, B, C = map(int, sys.stdin.readline().split())

def power(x, n):

    # base case:
    if n == 0:
        return 1

    if n % 2 == 0:
        half = power(x, n // 2)
        return (half*half) % C

    else:
        half = power(x, (n-1) // 2)
        return (half * half) * x % C

print(power(A, B))

