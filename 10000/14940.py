# 14940: 쉬운 최단거리

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split()) # n은 세로크기 m 은 가로크기

block = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

queue = deque()

for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(n):
    for j in range(m):
        if block[i][j] == 2:
            start = (i,j)
            visited[i][j] = 0
            queue.append(start)

        if block[i][j] == 0:
            visited[i][j] = 0



while queue:
    cury, curx = queue.popleft() # x 가로 y 세로
    block[cury][curx] = 0

    for nexty, nextx in (cury +1, curx), (cury, curx + 1), (cury -1, curx), (cury, curx-1):

        if 0 <= nextx < m and 0 <= nexty < n and visited[nexty][nextx] == -1:
            visited[nexty][nextx] = visited[cury][curx] + 1
            queue.append((nexty, nextx))



for i in range(n):
    print(*visited[i])