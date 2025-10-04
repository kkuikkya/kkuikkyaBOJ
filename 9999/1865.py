# 1865: 웜홀

# 벨만포드 알고리즘 복습 & 가상노드 아이디어 생각.. 가상노드는 진짜 미친거같은데

import sys

def bellman_ford():
    N, M, W = map(int, sys.stdin.readline().split()) # N 노드 수 M 도로 수 W 웜홀 수

    edges = []

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append((S, E, -1 * T))

    distance = [float("inf") for _ in range(N+1)]
    distance[0] = 0

    for i in range(1, N+1):
        edges.append((0,i,0))

    for i in range(N+1):

        for cur, next, cost in edges:
            if distance[cur] != float("inf") and distance[cur] + cost < distance[next]:
                distance[next] = distance[cur] + cost

                if i == N:
                    return "YES"


    return "NO"



def main():
    
    TC = int(sys.stdin.readline())

    for _ in range(TC):
        print(bellman_ford())

main()