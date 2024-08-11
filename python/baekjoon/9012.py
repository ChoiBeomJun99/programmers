# 스택사용 문제
from collections import deque

T = int(input())
for i in range(T):
    case = input()
    
    stack = deque() #stack
    for i, v in enumerate(case):
        if not stack: #스택이 비어있을 시
            stack.append(v)
            continue
        
        if v == '(':
            stack.append(v)
        
        elif v == ')':
            if stack[-1] == '(':
                stack.pop()
        
    if stack:
        print('NO')
    else:
        print('YES')