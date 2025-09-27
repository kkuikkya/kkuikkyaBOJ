# 1753: 최단경로

import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline()) -1

graph = defaultdict(list)

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())

    s -= 1
    e -= 1

    graph[s].append((w, e))

minDistance = [float("inf") for _ in range(V)]


hp = []
heapq.heappush(hp, (0, start))
minDistance[start] = 0

while hp:
    curw, curp = heapq.heappop(hp)

    if minDistance[curp] < curw:
        continue

    for nw, np in graph[curp]:
        if 0 <= np < V and minDistance[np] > minDistance[curp] + nw:
            minDistance[np] = minDistance[curp] + nw
            heapq.heappush(hp, (minDistance[np], np))

for item in minDistance:
    if item == float("inf"):
        print("INF")
    else:
        print(item)
