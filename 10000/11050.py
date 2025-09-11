# 11050 이항 계수

def binomial(n, m):

    # base case
    if n == m or m == 0:
        return 1

    return binomial(n-1, m-1) + binomial(n-1, m)


# 과연 어디까지 뚫릴까 얘로
def binomialDP(n,m):
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)] # memo[i][j] 는 bimomial(i,j)

    for i in range(n+1):
        memo[i][0] = 1
        memo[i][i] = 1

    for i in range(2,n+1):
        for j in range(1, i):
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

    return memo[n][m]




n, m = map(int, input().split())

print(binomialDP(n,m))




