# BFS 문제
from collections import deque

def solution(maps):    
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 / 상:(-1, 0), 하:(1, 0), 좌:(0, -1), 우:(0, 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복 = 모든 칸을 다 이동했다는 것이다.
        while queue:
            x, y = queue.popleft()

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

                # 벽이면 무시하기
                if maps[nx][ny] == 0:  continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기 (이동 할 수 있는 경우.)
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1 # 거리 계산하기 (시작 점 부터 쌓아온 거리)
                    queue.append((nx, ny)) # 재귀

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[n-1][m-1] # 이 값이 1이면 방문을 못했다는 뜻이다.
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer


# try 2
# bfs 문제 
# from collections import deque

# # 상하좌우
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# def solution(maps):
#     answer = 0
    
#     n = len(maps) # 높이
#     m = len(maps[0]) # 폭
    
#     def bfs(x, y):
#         queue = deque()
#         queue.append((x,y))
        
#         while queue:
#             px, py = queue.popleft() # 이전 좌표 좌표
            
#             for i in range(4):
#                 nx, ny = px + dx[i], py+ dy[i]
                     
#                 if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1: # 처음 지나가는 유효한 길.
#                     maps[nx][ny] = maps[px][py] + 1
#                     queue.append((nx,ny))
        
#         return maps[n-1][m-1]
    
    
#     answer = bfs(0, 0)
#     return -1 if answer == 1 else answer