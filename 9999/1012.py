# 1012: 유기농 배추

import sys
from collections import deque

Moves  = [(1,0), (0,1), (-1,0), (0,-1)]

def cabbage():
    M, N, K = map(int, sys.stdin.readline().split())

    visited = [[False for _ in range(M)] for _ in range(N)] # 방문 플래그
    memo = [[0 for _ in range(M)] for _ in range(N)] # 배추 상태도 저장 memo[i][j] i 가로 j 세로

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        memo[y][x] = 1

    def inRange(x, y):
        return 0<= x < M and 0<= y < N

    def bfs(y,x): # 연결된 배추의 상태를 visited 로 바꾼다

        queue = deque()
        queue.append((y,x))

        while queue:

            y, x = queue.popleft()

            if visited[y][x]:
                continue

            visited[y][x] = True
            
            for move in Moves:
                movedx = x + move[0]
                movedy = y + move[1]

                if inRange(movedx, movedy):
                    if memo[movedy][movedx] and not visited[movedy][movedx]:
                        queue.append((movedy, movedx))

    worm = 0

    for i in range(M):
        for j in range(N):
            if memo[j][i] and not visited[j][i]:
                worm += 1
                bfs(j, i)

    print(worm)


T = int(sys.stdin.readline())
for _ in range(T):
    cabbage()

