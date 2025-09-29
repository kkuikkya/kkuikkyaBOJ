# 9663: N-Queen

import sys

n = int(sys.stdin.readline())
ans = 0
# pos[i] = j 는 i번 행, j번 열에 퀸을 놓았다는 의미
pos = [0] * n

def is_promising(row):
    # 0번 행부터 현재 직전 행(row-1)까지 확인
    for i in range(row):
        # 같은 열에 있거나, 대각선에 있는 경우
        if pos[i] == pos[row] or abs(pos[row] - pos[i]) == row - i:
            return False
    return True

def dfs(row):
    global ans
    
    # Base Case: 마지막 행까지 성공적으로 퀸을 놓은 경우
    if row == n:
        ans += 1
        return

    # 0번 열부터 (n-1)번 열까지 퀸을 놓는 것을 시도
    for col in range(n):
        pos[row] = col  # (row, col) 위치에 퀸을 놓아본다.
        
        # 만약 그 위치가 유망하다면
        if is_promising(row):
            # 다음 행으로 재귀 호출
            dfs(row + 1)
            # (재귀가 끝나고 돌아오면, pos[row]의 값은 다음 for loop에서 덮어써지므로
            # 별도의 '퀸 회수' 코드가 필요 없음)


# 0번 행부터 시작
dfs(0)
print(ans)