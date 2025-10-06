# 15663: N과 M(9)

import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort() # 입력 배열 정렬

visited = [False] * N
tmp = []

def dfs():
    # 1. 종료 조건: tmp의 길이가 M과 같아지면 출력
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return
    
    # 2. 중복 값 처리: 같은 레벨에서 이전에 사용한 값을 기억
    prev = 0 
    for i in range(N):
        # 3. 방문하지 않았고, 현재 탐색 레벨에서 이전에 사용한 값과 다를 경우에만 재귀 호출
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            tmp.append(arr[i])
            prev = arr[i] # 현재 값을 '사용한 값'으로 기록
            dfs()
            # 4. 백트래킹: 다음 탐색을 위해 상태를 원상 복구
            visited[i] = False
            tmp.pop()

dfs()