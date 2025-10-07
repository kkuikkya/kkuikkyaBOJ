# 1149: RGB 거리

import sys

def rgb_distance(k, pre): 

    if k == N:
        return 0

    if k == 0:

        case0 = arr[k][0] + rgb_distance(k+1,0)
        case1 = arr[k][1] + rgb_distance(k+1,1)
        case2 = arr[k][2] + rgb_distance(k+1,2)

        return min(case0, case1, case2)

    else: 
        case0 = float("inf")
        case1 = float("inf")
        case2 = float("inf")

        if pre == 0:
            case1 = arr[k][1] + rgb_distance(k+1,1)
            case2 = arr[k][2] + rgb_distance(k+1,2)

        elif pre == 1:
            case0 = arr[k][0] + rgb_distance(k+1,0)
            case2 = arr[k][2] + rgb_distance(k+1,2)
            
        elif pre == 2:
            case1 = arr[k][0] + rgb_distance(k+1,0)
            case2 = arr[k][1] + rgb_distance(k+1,1)

        return min(case0, case1, case2)

def rgb_distanceDP():

    dp = [[-1 for _ in range(3)] for _ in range(N)] # dp[i][color] 는 i 번째 까지 칠하고 i번째가 color 색으로 칠해져있을때 최소값

    # base case:
    for color in range(3):
        dp[0][color] = arr[0][color]


    # dp table 
    for i in range(1, N):
        
        for color in range(3):

            if color == 0:
                dp[i][color] = arr[i][color] + min(dp[i-1][1], dp[i-1][2])

            elif color == 1:
                dp[i][color] = arr[i][color] + min(dp[i-1][0], dp[i-1][2])

            elif color == 2:
                dp[i][color] = arr[i][color] + min(dp[i-1][0], dp[i-1][1])

    return min(dp[N-1])

N = int(sys.stdin.readline())
arr = [list(map(int, sys. stdin.readline().split())) for _ in range(N)]

print(rgb_distanceDP())


# dp 공간복잡도 최적화

# dp[0], dp[1], dp[2]가 각각 이전 집을 R, G, B로 칠했을 때의 최소 비용
dp = arr[0] 

for i in range(1, N):
    # 이전 단계의 최소 비용을 임시 변수에 저장
    prev_r, prev_g, prev_b = dp[0], dp[1], dp[2]
    
    # 현재 단계의 최소 비용을 갱신
    # 현재 집을 R로 칠하는 비용 + min(이전 집을 G로, 이전 집을 B로)
    dp[0] = arr[i][0] + min(prev_g, prev_b)
    
    # 현재 집을 G로 칠하는 비용 + min(이전 집을 R로, 이전 집을 B로)
    dp[1] = arr[i][1] + min(prev_r, prev_b)
    
    # 현재 집을 B로 칠하는 비용 + min(이전 집을 R로, 이전 집을 G로)
    dp[2] = arr[i][2] + min(prev_r, prev_g)

print(min(dp))