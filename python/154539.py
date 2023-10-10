# 시간 초과 유도 문제, 자신의 뒤를 이어가면서 해야하므로 스택을 활용한다.
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i, v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            answer[stack.pop()] = v
        stack.append(i)
    
    return answer