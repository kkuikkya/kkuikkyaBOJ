# 1509: 팰린드롬 분할

import sys

arr = list(sys.stdin.readline().rstrip())
N = len(arr)

is_palindrome = [[0 for _ in range(N)] for _ in range(N)] # dp[i][j] 는 i가 시작인덱스고 j 가 끝인덱스일때 팰린드롬인지 저장


# base case: 문자열이 1개일경우 팰린드롬
for i in range(N):
    is_palindrome[i][i] = 1

# base case2: 같은 문자열이 2개 있을 경우 팰린드롬
for i in range(N - 1):
    if arr[i] == arr[i+1]:
        is_palindrome[i][i+1] = 1

# 재귀 단계, 양옆의 문자가 같다면 팰린드롬
for length in range(3, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        if arr[i] == arr[j] and is_palindrome[i+1][j-1] == 1:
            is_palindrome[i][j] = 1


# dp[i]: 0부터 i까지의 부분 문자열의 최소 팰린드롬 분할 개수
dp = [0] * N 

# base case: 글자가 한개일 때는 항상 한개
dp[0] = 1

# 재귀 단계, 전에 회문있는 경우에 그 때 dp[i]의 값이 줄어들 가능성이 생김
for i in range(1, N):
    dp[i] = dp[i-1] + 1 
    
    for j in range(i):
        if is_palindrome[j][i]:
            # j가 0 이면 자체가 팰린드롬
            if j == 0:
                dp[i] = 1
        
            # j-1까지의 최소 개수에 j~i까지의 팰린드롬을 더한 값과 비교
            else:
                dp[i] = min(dp[i], dp[j-1] + 1)

print(dp[N-1])