# 1920: 수 찾기
""" N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오."""
import sys

# 이진 탐색 처음 구현해봄
def binarySearch(arr, x):

    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s + e) // 2
        
        if arr[mid] == x:
            return True

        elif arr[mid] > x:
            e = mid - 1
            
        else:
            s = mid + 1

    return False



n = int(sys.stdin.readline())


arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

n = int(sys.stdin.readline())

arrFind = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    if binarySearch(arr, arrFind[i]):
        print(1)
    
    else:
        print(0)

