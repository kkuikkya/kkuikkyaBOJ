# 2606: 바이러스

# 그래프, 연결되어있는 컴퓨터 수 구하기

import sys
from collections import deque
from collections import defaultdict

n = int(sys.stdin.readline())
nEdge = int(sys.stdin.readline())

# 일반적인 딕셔너리는 key 없이 접근할경우 오류가 나지만 얘는 자체 초기화
graph = defaultdict(list)

for i in range(nEdge):
    key, value = map(int, sys.stdin.readline().split())
    
    # 그래서 이렇게 작성해도 아무 문제가 없음
    graph[key].append(value)
    graph[value].append(key)

queue = deque()
queue.append(1)

visited = set()
visited.add(1)

# BFS 이런 문제는 DFS 시행시 모든 경우의 수를 다 따져봐야하기 때문에 오래 걸릴 수 있음
while queue:
    x = queue.popleft()

    for i in graph[x]:
        if i not in visited:
            visited.add(i)
            queue.append(i)

print(len(visited) -1)
