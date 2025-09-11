# 2609 최대공약수와 최소공배수

# 최대공약수 -> 유클리드 호제법 / 최소공배수 브루트포스?

n1, n2 = map(int, input().split())

if n1 < n2:
    n1, n2 = n2, n1

a, b = n1, n2

while b > 0:

    a, b = b, a % b

gcd = a


print(gcd)
print(n1 * n2 // gcd)
