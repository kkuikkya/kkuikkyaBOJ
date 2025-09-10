# 1259 팰린드롬수 


while True:
    n = input()

    if int(n) == 0:
        break

    if n == n[::-1]:
        print("yes")

    else:
        print("no")