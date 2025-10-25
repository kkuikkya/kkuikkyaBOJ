# 2252: 줄 세우기

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())

    graph[e].append(s)

visited = [False for _ in range(N+1)]

def DFS(start):
    """한 노드에 대해 더 이상 선행 노드가 없다면 그 노드를 출력합니다"""

    visited[start] = True

    for next_node in graph[start]:
        if not visited[next_node]:
            DFS(next_node)
            
    print(start, end = " ")
        

for i in range(1, N+1):

    if not visited[i]:
        DFS(i)

print()
