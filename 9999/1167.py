# 1167: 트리의 지름

import sys
from collections import defaultdict, deque

V = int(sys.stdin.readline())
arr = []
graph = defaultdict(list)

for i in range(V):
    arr.append(list(map(int, sys.stdin.readline().split())))

    pnt = 1

    while arr[i][pnt] != -1:
        graph[arr[i][0]].append((arr[i][pnt+1], arr[i][pnt]))
        pnt += 2

def dfs(N): # 시작 노드 N에대해 가장 긴 길이를 반환합니다
    visited = [0 for _ in range(V+1)]
    visited[N] = 1
    stack = deque()
    stack.append((0, N))

    dfs_max = 0

    while stack:

        curw, curp = stack.pop()

        if curw > dfs_max:
            dfs_max = curw
            dfs_maxp = curp

        for nw, np in graph[curp]:
            if not visited[np]:
                visited[np] = True
                
                stack.append((curw + nw, np))

    return dfs_max, dfs_maxp

last, lastp = dfs(1)

maxd, maxp = dfs(lastp)

print(maxd)