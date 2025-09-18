# 11726: 2n 타일링

"""다이내믹 프로그래밍 완전정복에서 수도없이 봤던 문제"""

import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(max(3,n + 1))]

dp[1] = 1
dp[2] = 2

for i in range(3, n+ 1):
    dp[i] = dp[i-1] + dp [i-2]

print(dp[n] % 10007)