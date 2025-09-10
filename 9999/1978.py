# 1978 소수찾기

n = int(input())

arr = map(int, input().split())

primary = [2,3]

for i in range(4, 1001):
    for j in primary:
        if i % j == 0:
            break

    else:
        primary.append(i)

result = []

for i in arr:
    if i in primary:
        result.append(i)

print(len(result))


# 1978 소수 찾기 - 에라토스테네스의 체 활용

n = int(input())
numb = list(map(int, input().split()))

# 처음에는 0과 1을 제외한 모든 수가 소수(True)라고 가정
isPrime = [True] * 1001
isPrime[0] = isPrime[1] = False  # 0과 1은 제외

# 2부터 1000의 제곱근(약 31.6)까지만 확인
for i in range(2, int(1001**0.5) + 1):
    # i가 소수인 경우
    if isPrime[i]:
        # i의 배수들을 모두 소수가 아니라고 표시
        # j는 2부터 시작하여 i*j가 1000을 넘지 않을 때까지 반복
        for j in range(i * 2, 1001, i):
            isPrime[j] = False

# 입력받은 수들 중에서 소수의 개수
count = 0
for i in numb:
    if isPrime[i]:
        count += 1

print(count)