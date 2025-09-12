# 10814 나이순 정렬

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    arr.append([int(age), name])

# 안정정렬이기 때문에 입력순서는 유지된채로 정렬
arr.sort(key=lambda x: x[0])

for i in range(n):
    print(arr[i][0], arr[i][1])