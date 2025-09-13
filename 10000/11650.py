# 11650: 좌표 정렬하기

"""2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오."""

import sys


# mergeSort
def mergeSort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    leftArr = mergeSort(arr[:mid])
    rightArr = mergeSort(arr[mid:])

    return merge(leftArr, rightArr)

def merge(leftArr, rightArr):

    left = 0
    right = 0

    merged = []

    while left < len(leftArr) and right < len(rightArr):

        if leftArr[left][0] < rightArr[right][0]:
            merged.append(leftArr[left])
            left += 1

        elif leftArr[left][0] == rightArr[right][0]:

            if leftArr[left][1] < rightArr[right][1]:
                merged.append(leftArr[left])
                left += 1

            else:
                merged.append(rightArr[right])
                right += 1


        else:
            merged.append(rightArr[right])
            right += 1

    
    merged += leftArr[left:]
    merged += rightArr[right:]

    return merged


n = int(sys.stdin.readline())

tmp = []

for i in range(n):
    tmp.append(list(map(int,sys.stdin.readline().split())))

merged = mergeSort(tmp)

for i in merged:
    print(i[0], i[1])
