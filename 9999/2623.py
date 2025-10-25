import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())

# 1. 그래프(정방향) 및 진입 차수(indegree) 배열 초기화
graph = defaultdict(list)
indegree = [0] * (N + 1)

# 2. 그래프 생성 및 진입 차수 계산
for _ in range(M):
    tmp = list(map(int, sys.stdin.readline().split()))
    # tmp[0]은 가수의 수, tmp[1]부터 순서

    for j in range(1, len(tmp) - 1):
        A = tmp[j]
        B = tmp[j+1]
        graph[A].append(B) # A -> B
        indegree[B] += 1   # B의 진입 차수 증가

# 3. 위상 정렬
queue = deque()
result = []

# 4. 진입 차수가 0인 노드(시작점)를 큐에 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 5. 큐를 이용한 위상 정렬
while queue:
    curr = queue.popleft()
    result.append(curr) # 결과 리스트에 추가

    # 현재 노드와 연결된 노드들의 진입 차수 1 감소
    for next_node in graph[curr]:
        indegree[next_node] -= 1
        
        # 새롭게 진입 차수가 0이 된 노드를 큐에 추가
        if indegree[next_node] == 0:
            queue.append(next_node)

# 6. 결과 출력
if len(result) == N:
    for node in result:
        print(node)
else:
    # 큐가 비었는데 result에 N개가 다 안 담겼다면 사이클이 존재
    print(0)