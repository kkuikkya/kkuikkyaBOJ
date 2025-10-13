# 7453: 합이 0인 네 정수

import sys

n = int(sys.stdin.readline())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# 두 배열씩 짝지어서 합을 구합니다
ab_sums = []
cd_sums = []
for i in range(n):
    for j in range(n):
        ab_sums.append(A[i] + B[j])
        cd_sums.append(C[i] + D[j])

# 우선 두 리스트를 모두 정렬합니다
ab_sums.sort()
cd_sums.sort()

# 투포인터로 개수를 찾습니다
count = 0
left = 0
right = len(cd_sums) - 1

while left < len(ab_sums) and right >= 0:
    current_sum = ab_sums[left] + cd_sums[right]
    
    if current_sum == 0:
        # ab_sums 쪽 중복 값 개수 세기
        ab_target = ab_sums[left]
        ab_count = 0
        while left < len(ab_sums) and ab_sums[left] == ab_target:
            ab_count += 1
            left += 1
        
        # cd_sums 쪽 중복 값 개수 세기
        cd_target = cd_sums[right]
        cd_count = 0
        while right >= 0 and cd_sums[right] == cd_target:
            cd_count += 1
            right -= 1
            
        count += ab_count * cd_count

    elif current_sum < 0:
        left += 1
    else: # current_sum > 0
        right -= 1

print(count)