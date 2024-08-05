#스택을 이용하면 된다.
from collections import deque

N = int(input())
answer = 0

for _ in range(N):
    case = input()
    stack = deque()

    for i in case:
        if not stack: #비어있을 시
            stack.append(i)
            continue
        
        if stack[-1] == i: #비어있지 않고, 바로 전과 같은 문자일때
            stack.pop()
        else: #비어있지 않고, 바로 전과 다른 문자일때
            stack.append(i)
    
    if not stack:
        answer += 1

print(answer)