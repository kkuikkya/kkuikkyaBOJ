# 15654: N과 M(5)

import sys

N, M = map(int,sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

tmp = []
visited = [False] * N 

def dfs(): # tmp 는 이미 보관중인 아이템

    if len(tmp) == M: # 조건이 만족되면 출력 후 종료
        print(*tmp)
        return

    # dfs: 모든 원소를 루프하고 이미 보관중이지 않다면 백트래킹
    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            tmp.append(arr[i])
            dfs()
            tmp.pop()
            visited[i] = False


dfs()