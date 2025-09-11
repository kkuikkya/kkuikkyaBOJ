# 1181 단어 정렬
# 아 분하다 다음에는 꼭 내가 구현해서 풀어야지... 아니 솔직히 실버5 문제인데 안에 왜 정렬 문제가 같이 있는거임? ㅈㄴ 너무해


n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))

arr.sort()
arr.sort(key = len)

for i in arr:
    print(i)
