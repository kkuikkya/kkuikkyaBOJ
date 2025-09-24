# 14003 가장 긴 증가하는 부분 수열
import sys
from bisect import bisect_left # 이분 탐색

# 입력 처리
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# lis: 각 길이일때 LIS의 마지막 숫자가 가장 작은 경우 ex) lis[2] 는 길이가 3일때 마지막 원소
lis = []

# path[i]: arr[i]가 lis 배열에 들어갈 때의 인덱스를 저장
path = []

for num in arr:
    if not lis or num > lis[-1]:
        path.append(len(lis))
        lis.append(num)
    else:
        # 각 원소가 마지막일 때 나오는 길이
        idx = bisect_left(lis, num) # lowerBound
        lis[idx] = num 
        path.append(idx) 

# LIS의 길이는 lis 배열의 길이
lis_length = len(lis)
print(lis_length)
