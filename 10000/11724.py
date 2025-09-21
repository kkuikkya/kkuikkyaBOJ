# 11724: 연결 요소의 개수

import sys
from collections import defaultdict

N, M = map(int,sys.stdin.readline().split())

graph = defaultdict(list)

for i in range(M):
    key, value = map(int, sys.stdin.readline().split())
    
    graph[key].append(value)
    graph[value].append(key)

visited = set()

def DFS(start_node):
    # 탐색할 노드를 담아둘 스택
    stack = [start_node]
    
    while stack:
        # 스택의 가장 마지막 노드를 꺼냅니다 (LIFO: Last-In, First-Out)
        v = stack.pop()
        
        # 만약 이미 방문했다면 건너뜁니다.
        if v in visited:
            continue
        
        visited.add(v)
        
        # 연결된 노드들을 스택에 추가합니다.
        # pop() 순서를 고려하여 역순으로 넣거나, 순서가 상관없다면 그냥 넣어도 됩니다.
        for i in reversed(graph[v]):
            if i not in visited:
                stack.append(i)
count = 0

for i in range(1, N+1):

    if i not in visited:
        count += 1
        DFS(i)

print(count)
