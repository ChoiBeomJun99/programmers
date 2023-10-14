# DFS, BFS 두 방향을 풀 수 있는 문제이다.
from collections import deque

# BFS 풀이 (queue 이용)
def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    queue = deque()    
    queue.append([numbers[0], 0]) # 양수
    queue.append([-1 *numbers[0], 0]) # 음수
        
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if target == temp:
                answer += 1
                
    return answer


# DFS 풀이
# def solution(numbers, target):    
#     n = len(numbers)
#     answer = 0
    
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
        
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
    
#     dfs(0,0)
#     return answer


# BFS 활용하기
from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers) - 1
    
    queue = deque()
    queue.append([numbers[0], 0]) # 양의 값과 idx
    queue.append([numbers[0] * -1, 0]) # 음의 값과 idx
    
    while queue:
        value, idx = queue.popleft()
        
        if n == idx:
            # 끝까지 더하고 뺐으므로, 타겟과 비교하기
            if target == value:
                answer += 1
        else:
            queue.append([value + numbers[idx+1], idx+1])
            queue.append([value - numbers[idx+1], idx+1])
    
    return answer