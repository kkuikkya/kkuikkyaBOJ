# 4153 직각삼각형

while True:
    arr = list(map(int, input().split()))
    arr = sorted(arr)

    if not(arr[0] or arr[1] or arr[2]):
        break

    if arr[0]*arr[0] + arr[1]*arr[1] == arr[2]*arr[2]:
        print("right")

    else:
        print("wrong")
