# 1074: Z

import sys

def findZ(N, r, c): # 2**N: 사각현 한 변 길이 r 행 c 열

    # base case
    if N == 1:
        if r == 0 and c == 0:
            return 0

        elif r == 0 and c == 1:
            return 1

        elif r == 1 and c == 0:
            return 2
        
        elif r == 1 and c == 1:
            return 3

    result = 0

    newr = r
    newc = c

    length = 2**N
    halfLen = length // 2

    if r >= halfLen:
        newr = r - halfLen
        result += 2*(halfLen**2)

    if c >= halfLen:
        newc = c - halfLen
        result += halfLen**2

    return result + findZ(N - 1, newr, newc)

N, r, c = map(int, sys.stdin.readline().split())

print(findZ(N, r, c))
    
