# 15650: N과 M(2)

import sys

def dfs(rest, tmp, s):

    if rest == 0:
        result.append(tmp)
        return

    if N - s < rest or s == N:
        return 
    
    dfs(rest -1, tmp + [arr[s]], s + 1)
    dfs(rest, tmp, s + 1)

N, M = map(int, sys.stdin.readline().split())

arr = list(range(1,N + 1))

result = []

dfs(M, [], 0)

for item in result:
    for i in item:
        print(i, end = " ")
    print()

    



# 더 정석적인 풀이

import sys

def dfs(start):
    # 1. 종료 조건: M개의 숫자를 모두 골랐다면
    if len(temp) == M:
        print(*temp) # 리스트의 원소를 공백으로 구분하여 출력
        return

    # 2. 재귀 호출: 다음 숫자를 선택
    # start부터 N까지의 숫자를 탐색
    for i in range(start, N + 1):
        temp.append(i) # 현재 숫자 추가
        dfs(i + 1)     # 다음 숫자는 현재 숫자+1 부터 탐색
        temp.pop()     # 돌아가기 (백트래킹)

N, M = map(int, sys.stdin.readline().split())
temp = [] # 조합을 임시로 저장할 리스트

dfs(1) # 1부터 탐색 시작