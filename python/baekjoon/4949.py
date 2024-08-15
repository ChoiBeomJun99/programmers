# .이 나올때까지 검사하기. 
from collections import deque

while True:
    case = str(input()) #문자열의 형태로 받아온다.
    
    if case == ".": #종료조건
        exit()
        break
    
    stack = deque() # 해결할 스택
    for i, word in enumerate(case):
        
        if word == "(" or word == "[":
            stack.append(word)
        
        if word == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(word)
                
        if word == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(word)
                    
    if not stack:
        print("yes")
    else:
        print("no")
            
        
        