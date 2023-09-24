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