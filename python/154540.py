#BFS 문제
from collections import deque

# 상하좌우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def solution(maps):
    answer = []    
    n, m = len(maps), len(maps[0]) # 높이, 폭
    visited = [m * [0] for _ in range(n)]
    
    
    def bfs(i, j):
        queue = deque()
        queue.append((i,j)) #시작점
        
        visited[i][j] = 1
        area = int(maps[i][j])
        
        while queue:
            pi, pj = queue.popleft()
            
            for k in range(4): # 상하좌우
                ni, nj = pi + di[k], pj + dj[k]
                
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                    area += int(maps[ni][nj])
                    visited[ni][nj] = 1
                    queue.append((ni,nj))
        
        return area
    
    for i in range(n): # 높이
        for j in range(m): # 폭
            if maps[i][j] != 'X' and visited[i][j] == 0: # 방문하지 않았으면
                answer.append(bfs(i, j))
                
    answer.sort()
    return [-1] if not answer else answer