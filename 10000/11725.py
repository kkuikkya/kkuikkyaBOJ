# 11725: 트리의 부모 찾기

import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
graph = defaultdict(list)

for i in range(N-1):
    parent, child = map(int, sys.stdin.readline().split())

    graph[child].append(parent)
    graph[parent].append(child) # 그래프 간선 추가(양방향 어느것이 부모인지 알 수 없으므로)

parent = [0 for _ in range(N+1)]

queue = deque()
queue.append(1)
parent[1] = 1 # 1번 노드 방문처리

while queue: # BFS
    cur = queue.popleft()

    for next in graph[cur]:
        if parent[next] == 0:
            parent[next] = cur
            queue.append(next)

for i in range(2, N+1):
    print(parent[i])