# 2630: 색종이 자르기

import sys

def cutting(sx, sy, length):

    if length == 0:
        return (0,0)

    def isAll(sx, sy, length):
        first = arr[sy][sx]

        for x in range(sx, sx + length):
            for y in range(sy, sy + length):

                if arr[y][x] != first:
                    return False

        else:
            return True

    # base case
    if isAll(sx, sy, length):
        if arr[sy][sx] == 1:
            return (1, 0)

        else:
            return (0,1)
        
    newlen = length // 2
    q1 = cutting(sx, sy, newlen)
    q2 = cutting(sx + newlen, sy, newlen)
    q3 = cutting(sx, sy + newlen, newlen)
    q4 = cutting(sx + newlen, sy + newlen, newlen)

    blueCount = q1[0] + q2[0] + q3[0] + q4[0]
    whiteCount = q1[1] + q2[1] + q3[1] + q4[1]



    return (blueCount, whiteCount)


n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

result = cutting(0,0,n)
print(result[1])
print(result[0])