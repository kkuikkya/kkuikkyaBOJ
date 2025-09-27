# 13549: 숨바꼭질 3

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

MAX = 100001

arr = [float("inf") for _ in range(MAX)]

arr[N] = 0 # 시작점 비용 0

heap = []
heapq.heappush(heap, (0, N))

if K < N:
    print(N - K)
    exit()

while heap:

    curw, cur = heapq.heappop(heap)

    if curw > arr[cur]:
        continue

 # Case 1: 순간이동 (비용 0)
    next = cur * 2
    if 0 <= next < MAX and arr[next] > curw:
        arr[next] = curw # 비용이 0이므로 현재 시간 그대로
        heapq.heappush(heap, (arr[next], next))

    # Case 2: 뒤로 걷기 (비용 1)
    next = cur - 1
    if 0 <= next < MAX and arr[next] > curw + 1:
        arr[next] = curw + 1 
        heapq.heappush(heap, (arr[next], next))
            
    # Case 3: 앞으로 걷기 (비용 1)
    next = cur + 1
    if 0 <= next < MAX and arr[next] > curw + 1:
        arr[next] = curw + 1
        heapq.heappush(heap, (arr[next], next))

print(arr[K])