# 18870: 좌표 압축

import sys
import bisect

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

setlist = sorted(list(set(arr)))

for i in range(N):
    x = bisect.bisect_left(setlist, arr[i])
    print(x, end = " ")
print()


# 다른 방법 / 이게 더 좋은 거 같기도..?

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 1. 정렬된 고유 값 리스트 생성 (동일)
setlist = sorted(list(set(arr)))

# 2. 각 값에 대한 인덱스(압축된 좌표)를 딕셔너리에 저장
# {값: 인덱스, ...} 형태, 예: {-10: 0, -9: 1, 2: 2, 4: 3}
coord_map = {value: i for i, value in enumerate(setlist)}
# enumerate는 인덱스와 값을 하나의 튜플로 반환(인덱스는 start 파라미터로 0이 기본값 다음 아이템마다 하나씩 증가)

# 3. 원래 배열을 순회하며 딕셔너리에서 압축된 좌표를 찾아 출력
for x in arr:
    print(coord_map[x], end=" ")
print()

