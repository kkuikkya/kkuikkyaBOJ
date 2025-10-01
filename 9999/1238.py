# 1238: 파티

import sys, heapq
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    s -= 1
    e -= 1

    graph[s].append((t,e))


def deikstra(s):
    hq = []
    visited = [float("inf") for _ in range(N)]

    heapq.heappush(hq, (0,s))

    while hq:
        curt, curp = heapq.heappop(hq)

        if visited[curp] < curt:
            continue

        visited[curp] = curt

        for nt, np in graph[curp]:

            if visited[np] > nt + curt:
                visited[np] = nt + curt
                heapq.heappush(hq, (visited[np], np))

    return visited, max(visited)

X_deiks, _ = deikstra(X-1)

for i in range(len(X_deiks)):
    X_deiks[i] += deikstra(i)[0][X-1]

print(max(X_deiks))



# 더 좋은 풀이

import sys, heapq
from collections import defaultdict

N, M, X = map(int, sys.stdin.readline().split())
X -= 1 # 인덱스 조정

# 원래 방향 그래프와 뒤집은 방향 그래프를 모두 만듭니다.
graph = defaultdict(list)
reversed_graph = defaultdict(list)

for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    s -= 1
    e -= 1
    graph[s].append((t, e))
    reversed_graph[e].append((t, s)) # 간선 방향을 뒤집어 저장

# 다익스트라 함수는 이제 그래프를 인자로 받도록 수정합니다.
def dijkstra(start_node, target_graph):
    distances = [float("inf")] * N
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        dist, node = heapq.heappop(pq)

        if distances[node] < dist:
            continue

        for weight, neighbor in target_graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances

# 1. 집 -> 파티 장소 (뒤집은 그래프에서 X부터 출발)
dist_to_party = dijkstra(X, reversed_graph)

# 2. 파티 장소 -> 집 (원래 그래프에서 X부터 출발)
dist_from_party = dijkstra(X, graph)

# 3. 왕복 시간 계산 및 최댓값 찾기
max_time = 0
for i in range(N):
    total_time = dist_to_party[i] + dist_from_party[i]
    if total_time > max_time:
        max_time = total_time

print(max_time)

