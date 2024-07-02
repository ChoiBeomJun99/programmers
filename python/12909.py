from collections import deque

def solution(s):
    answer = True
    stack = deque()
    
    for i in s:
        if not stack or i == '(':
            stack.append(i)
        else: 
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    
    return len(stack) == 0