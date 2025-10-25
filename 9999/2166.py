# 2166: 다각형의 면적

import sys

N = int(sys.stdin.readline())
figure = []

for _ in range(N):
    figure.append(list(map(int,input().split())))
figure.append(figure[0])


# 신발끈
answer = 0
for i in range(N):
    answer += figure[i][0]*figure[i+1][1] - figure[i+1][0]*figure[i][1]

print(abs(answer)/2)