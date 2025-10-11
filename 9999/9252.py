# 9252: LCS2

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
    pathA = [] # 같은 문자열을 발견해서 LCS가 하나 늘어날 때의 A의 인덱스
    pathB = [] # 같은 문자열을 발견해서 LCS가 하나 늘어날 때의 B의 인덱스

    for i in range(1, nA + 1):
        for j in range(1, nB + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    if dp[nA][nB] == 0:
        return 0, ""

    # LCS 길이
    lcs_len = dp[nA][nB]
    if lcs_len == 0:
        return 0, ""

    # DP 테이블 역추적 (백트래킹)
    lcs_str = []
    i, j = nA, nB
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]: # 위쪽 칸과 값이 같다면 위로 이동
            i -= 1
        elif dp[i][j] == dp[i][j-1]: # 왼쪽 칸과 값이 같다면 왼쪽으로 이동
            j -= 1
        else: # 위쪽, 왼쪽 칸과 모두 값이 다르다면 대각선에서 온 것 (문자가 같은 경우)
            lcs_str.append(A[i-1])
            i -= 1
            j -= 1
            
    # 문자를 역순으로 찾았으므로 뒤집어서 합침
    return lcs_len, "".join(reversed(lcs_str))


A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

lenLCS, LCS= LCSDP(A, B)

print(lenLCS)
print(LCS)

