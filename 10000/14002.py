# 14002 가장 긴 증가하는 부분 수열

def LMIS2(arr):

    memo = [1 for _ in range(len(arr))] # memo[i] 는 i 번쨰 원소로 끝나는 LMS

    # arr[j] 보다 arr[i] 가 더 커 이어붙일 수 있고 memo[j]에 1을 더한 값이 현재 값보다 크다면 값을 갱신합니다
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i] and memo[j] + 1 >= memo[i]:
                memo[i] = memo[j] + 1
    
    maxVal = max(memo)
    maxidx = memo.index(maxVal)
    result = [arr[maxidx]]
    recent = maxidx

    # 백트래킹을 통해 원소 값들을 찾습니다
    for i in range(maxidx ,-1, -1):
        if arr[i] < arr[recent] and memo[i] == memo[recent] - 1:
            result = [arr[i]] + result
            recent = i

    print(max(memo))

    for i in result:
        print(i, end = " ")

    return max(memo)


n = int(input())

arr = list(map(int, input().split()))

LMIS2(arr)