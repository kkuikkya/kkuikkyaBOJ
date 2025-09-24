# 9251: LCS

import sys

def LCS(A, B):
    if not A or not B:
        return 0

    if A[0] == B[0]:
        return 1 + LCS(A[1:], B[1:])

    else:
        return max(LCS(A[1:], B), LCS(A, B[1:]))


def LCSDP(A, B):
    nA = len(A)
    nB = len(B)

    dp = [[0 for _ in range(nB + 1)] for _ in range(nA + 1)] # dp[i][j] 는 A를 i 까지 B를 j 길이 만큼 사용했을때의 최대 LCS

    for i in range(1, nA + 1):
        for j in range(1, nB + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[nA][nB]

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

print(LCSDP(A, B))
