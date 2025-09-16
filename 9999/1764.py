# 1764: 듣보잡

"""김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오."""

import sys

n, m = map(int, sys.stdin.readline().split())

listen = set()

for i in range(n):
    listen.add(sys.stdin.readline().rstrip())

watch = set()

for j in range(m):
    watch.add(sys.stdin.readline().rstrip())

result = list(listen.intersection(watch))
result.sort()

print(len(result))
for item in result:
    print(item)
