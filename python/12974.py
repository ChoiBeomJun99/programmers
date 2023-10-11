from collections import deque

def solution(s):
    answer = 1
    stack = deque()
    
    for i, v in enumerate(s):
        if not stack:
            stack.append(v)
            continue
        
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
        
    if stack:
        answer = 0
    else:
        answer = 1

    return answer