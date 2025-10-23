# 1202: 보석 도둑

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

valueArr = []
maxWeigh = []

for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(valueArr, (M, V))

for i in range(K):
    C = int(sys.stdin.readline())
    maxWeigh.append(C)
    
maxWeigh.sort()

# 각 가방에 대해 넣을 수 있는 가장 큰 무게를 넣습니다

maxval = 0
candidates = []

for capacity in maxWeigh:

    while valueArr and valueArr[0][0] <= capacity:

        w, v = heapq.heappop(valueArr)
        heapq.heappush(candidates, -v)

    if candidates:
        maxval += - heapq.heappop(candidates)

print(maxval)

    
