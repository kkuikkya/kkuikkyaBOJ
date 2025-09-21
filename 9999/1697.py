# 1697: 숨바꼭질

import sys
from collections import deque

MAX = 100001

def hide_and_seek(N, K):
    # 예외 처리: N이 K보다 크거나 같으면 걸어가는게 유일한 방법
    if N >= K:
        return N - K

    # 초기값 설정: -1은 아직 방문한적 없음을 의미
    time = [-1] * MAX
    
    # 시작점은 N
    queue = deque([N])
    time[N] = 0  # 시작점까지 걸리는 시간은 0초
    
    while queue:
        cur = queue.popleft()
        
        # 만약 현재 위치가 도착지라면, 탐색을 종료하고 결과 반환
        if cur == K:
            return time[K]
            
        # 다음 위치들을 탐색
        for next_pos in (cur - 1, cur + 1, cur * 2):
            # 다음 위치가 유효한 범위 안에 있고 아직 방문한 적이 없다면 (처음 만나는 게 무조건 최소 이동 경로, 가중치가 모두 같은 경우)
            if 0 <= next_pos < MAX and time[next_pos] == -1:
                # 방문 처리, 걸린 시간을 기록
                time[next_pos] = time[cur] + 1
                # 다음에 탐색할 대상으로 큐에 추가
                queue.append(next_pos)

# 메인 실행
N, K = map(int, sys.stdin.readline().split())
print(hide_and_seek(N, K))