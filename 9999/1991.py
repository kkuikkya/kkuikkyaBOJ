# 1991: 트리 순회

import sys
from collections import defaultdict


n = int(sys.stdin.readline())

graph = defaultdict(list)

for i in range(n):
    node, left, right = sys.stdin.readline().split()

    graph[node].append(left)
    graph[node].append(right)


def pre(node):

    print(node, end= "")

    if graph[node][0] != ".":
        pre(graph[node][0])

    if graph[node][1] != ".":
        pre(graph[node][1])


def inorder(node):

    if graph[node][0] != ".":
        inorder(graph[node][0])

    print(node, end= "")

    if graph[node][1] != ".":
        inorder(graph[node][1])

def backorder(node):
    
    if graph[node][0] != ".":
        backorder(graph[node][0])

    if graph[node][1] != ".":
        backorder(graph[node][1])

    print(node, end= "")

pre('A')
print()
inorder('A')
print()
backorder('A')
print()
    
    


