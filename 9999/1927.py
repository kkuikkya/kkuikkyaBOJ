# 1927: 최소 힙

import heapq
import sys

heap = []

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())

    if n == 0:
        if heap:
            smallest = heapq.heappop(heap)
            print(smallest)

        else:
            print(0)

    else:
        heapq.heappush(heap, n)

