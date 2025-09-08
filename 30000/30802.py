# 30802 웰컴 키트

n = int(input())

arr = list(map(int, input().split()))

t,p = map(int, input().split())

minT = 0
minP = 0
plusP = 0

for i in arr:
    if i % t == 0:
        minT += i // t

    else:
        minT += i // t + 1

minP = n // p
plusP = n % p

print(minT)
print(minP, plusP)



