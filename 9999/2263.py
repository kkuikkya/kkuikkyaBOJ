# 2263: 트리의 순회

# 아니 pypy3은 메모리 초과 나는대 python3은 메모리초과 안남 억울하다..
# 이는 실행환경의 차이때문인데 pypy3는 컴파일러처럼 작동함 (JIT)
# 그래서 속도는 빠르지만 이에대한 오버헤드가 발생해서 메모리 사용량이 많을 수 밖에 없음
# ㅋㅋ 일단 pypy3로 제출해보고 메모리초과나면 python3로 제출하는게 국룰 ㅋㅋ 

import sys
sys.setrecursionlimit(10**6) 

n = int(sys.stdin.readline()) # 정점 개수

inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))


inorder_idx = {value: i for i, value in enumerate(inorder)}


def preorder(ins, ine, pos, poe):
    
    if ins > ine or pos > poe:
        return

    root = postorder[poe]
    print(root, end = " ")
    
    rootidx = inorder_idx[root]
    
    leftsize = rootidx - ins

    preorder(ins, rootidx -1, pos, pos + leftsize - 1)
    preorder(rootidx+1, ine, pos + leftsize, poe - 1)


preorder(0, n-1, 0, n-1)
print()




