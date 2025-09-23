# 7576: 토마토
# 토맛토맛토 ㅋㅋ

import sys
from collections import deque

# bfs 로 풀 듯?

#main

M, N = map(int, sys.stdin.readline().split()) # M 가로, N 세로

tomato = []
memo = [[-2 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    tomato.append(list(map(int, sys.stdin.readline().split())))

# 만약 토마토가 처음부터 모두 익어있다면

zeroExists = any(0 in row for row in tomato)

if not zeroExists:
    print(0)
    sys.exit()
    

queue = deque() # bfs

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i,j))
            memo[i][j] = 0

while queue:
    y, x = queue.popleft()


    for (ny, nx) in (y + 1, x), (y, x + 1), (y -1, x), (y, x - 1):

        if 0<= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:

            memo[ny][nx] = memo[y][x] + 1
            tomato[ny][nx] = 1
            queue.append((ny,nx))

zeroExists = any(0 in row for row in tomato)

if zeroExists:
    print(-1)

else:
    maxTomato = 0

    for i in range(N):
        for j in range(M):
            if memo[i][j] > maxTomato:
                maxTomato = memo[i][j]


    print(maxTomato)

