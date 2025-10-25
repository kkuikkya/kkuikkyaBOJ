# 2473: 세 용액

import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

minlow = arr[0]
minmiddle = arr[N-2]
minhigh = arr[N-1]

minsum = minlow + minmiddle + minhigh

for middle in range(1, N-1):

    low = 0
    high = N-1
    
    while low < middle and middle < high:

        tmpsum = arr[low] + arr[middle] + arr[high]

        if abs(tmpsum) < abs(minsum):
            minsum = tmpsum
            minlow = arr[low]
            minmiddle = arr[middle]
            minhigh = arr[high]

        if tmpsum == 0:
            print(minlow, minmiddle, minhigh)
            exit()

        elif tmpsum < 0:
            low += 1

        else:
            high -= 1



print(minlow, minmiddle, minhigh)
    