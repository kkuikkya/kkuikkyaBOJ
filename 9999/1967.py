# 1967: 트리의 지름 // 어떻게 트리의 지름이 2개? 

import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    exit()

graph = defaultdict(list)

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().split())

    graph[p].append((w,c))
    graph[c].append((w,p))


def bfs(f):
    visited = [0 for _ in range(n+1)]
    visited[f] = 1

    queue = deque()
    queue.append((0, f)) # first node
    max_distance = 0

    while queue:
        curw, curp = queue.popleft()

        if max_distance < curw:
            max_distance = curw
            max_position = curp

        for nw, np in graph[curp]:
            if not visited[np]:
                visited[np] = nw + curw
                queue.append((visited[np], np))
    
    return max_distance, max_position

far_d, far_p = bfs(1)
result_d, result_p = bfs(far_p)

print(result_d)