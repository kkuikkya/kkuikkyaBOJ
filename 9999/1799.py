# 1799: 비숍
import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1. 비숍을 놓을 수 있는 위치를 흑백으로 미리 분리
white_squares = []
black_squares = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            # (행+열)이 짝수면 하얀색, 홀수면 검은색 (혹은 그 반대)
            if (r + c) % 2 == 0:
                white_squares.append((r, c))
            else:
                black_squares.append((r, c))

# 2. 대각선 사용 여부를 체크할 배열
diag1 = [False] * (2 * n - 1)  # r + c
diag2 = [False] * (2 * n - 1)  # r - c + (n - 1) 

# 백트래킹 결과를 저장할 변수
max_count = 0

def solve(index, count, squares):
    """
    index: 현재 확인 중인 squares 리스트의 인덱스
    count: 현재까지 놓은 비숍의 수
    squares: 탐색할 칸들의 좌표 리스트 
    """
    global max_count

    # 남은 칸에 전부 비숍을 놓아도 기존 최댓값을 못 넘으면 더 볼 필요 없음 Purning
    if len(squares) - index + count <= max_count:
        return

    # Base Case: 모든 칸을 다 확인했을 때
    if index == len(squares):
        max_count = max(max_count, count)
        return

    r, c = squares[index]

    # 현재 (r, c)에 비숍을 놓을 수 있는지 체크
    if not diag1[r + c] and not diag2[r - c + n - 1]:
        # 비숍을 놓는 경우
        diag1[r + c] = True
        diag2[r - c + n - 1] = True
        solve(index + 1, count + 1, squares)
        # 백트래킹, 놓았던 비숍을 다시 회수
        diag1[r + c] = False
        diag2[r - c + n - 1] = False

    # 비숍을 놓지 않는 경우
    solve(index + 1, count, squares)


# 하얀색 칸에 대해 최대 비숍 수 계산
solve(0, 0, white_squares)
white_max = max_count

# 변수 초기화 후 검은색 칸에 대해 계산
max_count = 0
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
solve(0, 0, black_squares)
black_max = max_count

# 두 결과를 더하면 최종답
print(white_max + black_max)







# 이렇게 풀어서는 시간복잡도 절대 해결 못합니다.. ㅜㅜ 검은칸과 흰칸으로 나누어서 생각해야 (N / 2)^2 가 되어 
# 풀 수 있어용
"""
# 1799: 비숍

import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bishop(): # (0,0) 부터 채우기 시작

    maxv = 0

    def recursive(i, j):
        nonlocal maxv

        if arr[i][j] == 1: # 1인 경우 놓는경우 안놓는 경우 모두 시도해야됨

            for v in 0, 2: # 비숍을 놓거나 놓지 않습니다
                
                if is_promising(i, j, v):
                    arr[i][j] = v

                    # base case
                    if i == n-1 and j == n-1:
                        nbishop = 0
                        for x in range(n):
                            for y in range(n):
                                if arr[x][y] == 2:
                                    nbishop += 1

                        if maxv < nbishop:
                            maxv = nbishop

                    elif j == n-1:
                        recursive(i+1, 0)

                    else:
                        recursive(i, j+1)
                
                arr[i][j] = 1
        
        else:
            # base case
            if i == n-1 and j == n-1:
                nbishop = 0
                for x in range(n):
                    for y in range(n):
                        if arr[x][y] == 2:
                            nbishop += 1

                if maxv < nbishop:
                    maxv = nbishop

            elif j == n-1:
                recursive(i+1, 0)

            else:
                recursive(i, j+1)

    def is_promising(i, j, v):

        if v == 0: # 비숍을 놓지 않는 경우 어느 경우에도 가능합니다
            return True
        
        if v == 2: # 비숍을 놓는 경우 다른 대각선에 비숍이 없어야합니다

            for x in range(i):
                for y in range(n):
                    if arr[x][y] == 2 and i - x == abs(j - y): # 대각선에 비숍이 있으면 안됩니다
                        return False 
                    
            return True # 겹치는 비숍이 없으면 참입니다
                        

    recursive(0,0)

    return maxv


    
print(bishop())
"""

    