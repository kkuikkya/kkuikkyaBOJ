# 1918: 후위 표기식

import sys
from collections import deque

string = sys.stdin.readline().rstrip()

stack = deque()

pnt= 0

while pnt < len(string):

    cur = string[pnt] # 현재 커서
    
    if cur == "+":
        # 우선순위가 더 높거나 같은 것들 제거
        while stack:
            if stack[-1] in "+-*/":
                x = stack.pop()
                print(x, end = "")

            else:
                break

        # 스택에 있는거 다 털어내고 스택에 새로 추가
        stack.append(cur)
    
    elif cur == "-":
        # 우선순위가 더 높거나 같은 것들 제거
        while stack:
            if stack[-1] in "+-*/":
                x = stack.pop()
                print(x, end= "")

            else:
                break

        # 스택에 있는거 다 털어내고 스택에 새로 추가
        stack.append(cur)

    elif cur == "*":
        # 우선순위가 더 높거나 같은 것들 제거(근데 우선순위가 같은 경우 밖에 없음)
        while stack:
            if stack[-1] in "*/":
                x = stack.pop()
                print(x, end= "")

            else:
                break

        stack.append(cur)


    elif cur == "/":
        # 우선순위가 더 높거나 같은 것들 제거(근데 우선순위가 같은 경우 밖에 없음)
        while stack:
            if stack[-1] in "*/":
                x = stack.pop()
                print(x, end= "")

            else:
                break

        stack.append(cur)

    # 괄호 시작 
    elif cur == "(":
        stack.append(cur)

    # 괄호 종료시에 괄호 안에 있던 연산자들 모두 출력
    elif cur == ")":
        while stack[-1] != "(":
            x = stack.pop()
            print(x, end= "")

        stack.pop()

    else:
        print(cur, end = "")
    
    pnt += 1 # 다음 커서

# 남은 연산자들 모두 처리
while stack:
    x = stack.pop()
    print(x, end= "")

# 줄바꿈
print()
    

# Refactoring

import sys
from collections import deque

string = sys.stdin.readline().rstrip()
stack = deque()
ans = ''

# 연산자 우선순위 설정
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for char in string:
    if 'A' <= char <= 'Z':  # 피연산자인 경우
        ans += char
    elif char == '(':      # 여는 괄호인 경우
        stack.append(char)
    elif char == ')':      # 닫는 괄호인 경우
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()  # '(' 제거
    else:  # 연산자인 경우
        # 스택의 top이 현재 연산자보다 우선순위가 높거나 같으면 계속 pop
        while stack and priority[stack[-1]] >= priority[char]:
            ans += stack.pop()
        stack.append(char)

# 스택에 남은 연산자 모두 출력
while stack:
    ans += stack.pop()

print(ans)