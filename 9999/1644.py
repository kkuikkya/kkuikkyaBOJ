# 1644: 소수의 연속합

import sys

N = int(sys.stdin.readline())

# 처음에는 0과 1을 제외한 모든 수가 소수(True)라고 가정
isPrime = [True] * (N + 1)
isPrime[0] = isPrime[1] = False  # 0과 1은 제외

for i in range(2, int((N)**0.5) + 1):
    # i가 소수인 경우
    if isPrime[i]:
        # i의 배수들을 모두 소수가 아니라고 표시
        for j in range(i * 2, N+1, i):
            isPrime[j] = False

onlyPrime = []

for i in range(len(isPrime)):

    if isPrime[i]:
        onlyPrime.append(i)

prime_prefix_sum = [0]

for i in range(len(onlyPrime)):
    prime_prefix_sum.append(prime_prefix_sum[i] + onlyPrime[i])

low = 0
high = 1
count = 0

while high < len(prime_prefix_sum):

    if prime_prefix_sum[high] - prime_prefix_sum[low] == N:
        count += 1
        high += 1

    elif prime_prefix_sum[high] - prime_prefix_sum[low] < N:
        high += 1

    else:
        low += 1

print(count)
