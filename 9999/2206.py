import sys
from collections import deque

def bfs():
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    if N == 1 and M == 1:
        return 1

    # visited[y][x][0] = 벽 안 부순 상태 방문 여부
    # visited[y][x][1] = 벽 부순 상태 방문 여부
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 0, 1))  # y, x, broken, count
    visited[0][0][0] = True

    while queue:
        y, x, broken, count = queue.popleft()

        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny, nx = y+dy, x+dx

            if 0 <= ny < N and 0 <= nx < M:
                # 목적지 도착
                if ny == N-1 and nx == M-1:
                    return count+1

                # 벽이 없고, 아직 방문 안 한 경우
                if arr[ny][nx] == 0 and not visited[ny][nx][broken] and not visited[ny][nx][0]:
                    visited[ny][nx][broken] = True
                    queue.append((ny, nx, broken, count+1))

                # 벽이 있고, 아직 부순 적이 없다면
                elif arr[ny][nx] == 1 and broken == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, 1, count+1))

    return -1

print(bfs())
