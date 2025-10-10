# 2239: 스도쿠

# 일단 기본 전략은 백트래킹
# 1. 각 칸에 1-9 까지 써본다
# 2. 위배되지 않으면 다음 칸으로 넘어간다
# 3. 위배되는 경우가 생기면 다시 삭제한다

import sys

def sdoku():
    arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]

    def is_promising(i, j, v): # 값이 유효한지 검사합니다
        for x in range(9): # 같은 행에 같은 값이 있다면 유망하지 않습니다
            if x == i:
                continue

            if arr[x][j] == v: 
                return False

        for y in range(9): # 같은 열에 같은 값이 있다면 유망하지 않습니다
            if y == j:
                continue

            if arr[i][y] == v: 
                return False

        if 0 <= i < 3 and 0 <= j < 3: # 1
            for x in range(3):
                for y in range(3):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 0 <= i < 3 and 3 <= j < 6: # 2
            for x in range(3):
                for y in range(3, 6):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 0 <= i < 3 and 6 <= j < 9: # 3
            for x in range(3):
                for y in range(6, 9):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 3 <= i < 6 and 0 <= j < 3: # 4
            for x in range(3, 6):
                for y in range(3):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 3 <= i < 6 and 3 <= j < 6: # 5
            for x in range(3,6):
                for y in range(3, 6):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 3 <= i < 6 and 6 <= j < 9: # 6
            for x in range(3, 6):
                for y in range(6, 9):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False
            
        elif 6 <= i < 9 and 0 <= j < 3: # 7
            for x in range(6, 9):
                for y in range(3):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 6 <= i < 9 and 3 <= j < 6: # 8
            for x in range(6, 9):
                for y in range(3, 6):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        elif 6 <= i < 9 and 6 <= j < 9: # 9
            for x in range(6, 9):
                for y in range(6, 9):
                    if x == i and y == j:
                        continue

                    if arr[x][y] == v:
                        return False

        return True

    def recursive(i, j): # 시작 지점
        
        if arr[i][j] == 0:

            for v in range(1,10): # 1부터 9 까지 놓아봅니다
                arr[i][j] = v

                if is_promising(i, j, v): # 값이 유망하다면 다음 값을 호출합니다

                    # base case
                    if i == 8 and j == 8:
                        for row in arr:
                            print("".join(map(str, row)))
                        exit()

                    elif j == 8:
                        recursive(i+1, 0)

                    else:
                        recursive(i, j+1)

                
                arr[i][j] = 0 # 다음 칸으로 넘어가서 실패해서 돌아왔다면, 내가 썼던 칸을 지웁니다

        else:
            if i == 8 and j == 8:
                for row in arr:
                    print("".join(map(str, row)))
                exit()

            elif j == 8:
                recursive(i+1, 0)

            else:
                recursive(i, j+1)

    recursive(0,0)
            


sdoku()



# 리팩토링

import sys

def solve(index):
    """
    미리 계산된 빈칸 목록(zeros)의 'index'번째 빈칸을 채우는 재귀 함수
    """
    
    # [Base Case] 모든 빈칸을 성공적으로 채웠을 경우
    if index == len(zeros):
        for row in board:
            print("".join(map(str, row)))
        # 답을 하나 찾았으므로 프로그램 즉시 종료
        sys.exit(0)

    # 이번에 채울 빈칸의 좌표를 목록에서 가져온다 (탐색 X)
    i, j = zeros[index]

    # 1부터 9까지의 숫자를 시도
    for v in range(1, 10):
        if is_promising(i, j, v):
            board[i][j] = v          # [전진] 숫자를 놓는다
            solve(index + 1)         # [탐색] 다음 빈칸을 채우러 간다
            board[i][j] = 0          # [후퇴] 막혔으면 놓았던 숫자를 다시 치운다

def is_promising(i, j, v):
    """(i, j) 위치에 숫자 v를 놓아도 유효한지 검사하는 함수"""
    
    # 1. 같은 행에 v가 있는지 검사
    for col in range(9):
        if board[i][col] == v:
            return False
            
    # 2. 같은 열에 v가 있는지 검사
    for row in range(9):
        if board[row][j] == v:
            return False
            
    # 3. 3x3 박스 안에 v가 있는지 검사
    start_row = (i // 3) * 3
    start_col = (j // 3) * 3
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if board[row][col] == v:
                return False
                
    return True

# --- 프로그램 시작점 ---

# 1. 스도쿠 보드 입력
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]

# 2. 앞으로 채워야 할 빈칸(0)들의 좌표 목록을 미리 계산
zeros = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]

# 3. 첫 번째 빈칸(index=0)부터 채우기 시작
solve(0)