# 10816: 숫자 카드 2

"""숫자 카드는 정수 하나가 적혀져 있는 카드이다.
 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오."""

import sys

# BSlower and upper 이거 매우 중요함 lower < 이고 upper 은 등호까지 포함해 그 다음 원소 
def binarySearchLowerBound(arr, x):

    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        else:
            high = mid
    
    return low


def binarySearchUpperBound(arr, x):

    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] <= x:
            low = mid + 1
            
        else:
            high = mid
    
    return low


n1 = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))


n2 = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

for i in arr2:
    lower = binarySearchLowerBound(arr1, i)
    upper = binarySearchUpperBound(arr1, i)
    print(upper - lower, end = " ")
