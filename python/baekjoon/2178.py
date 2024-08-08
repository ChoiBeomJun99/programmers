# 최단거리 ==> BFS문제이다.
# [위, 아래, 오른쪽, 왼쪽]
from collections import deque

N, M = map(int, input().split()) # N, M값 입력받기
graph = [list(map(int, ''.join(input().split()))) for i in range(N)] #입력받는 코드참고.

# BFS를 위한 초기값 set
dx = [0,0,1,-1] 
dy = [1,-1,0,0]

queue = deque([(0, 0)]) # 문제에서는 1,1 이지만, 실제 index는 0,0 부터 시작.

while queue:
    x, y = queue.popleft() #좌표
    
    for i in range(4):
        nextX, nextY = x + dx[i], y + dy[i]
        
        if 0 <= nextX < N and 0 <= nextY < M:
            if graph[nextX][nextY] == 1: #아직 방문 안한 경로인지 확인하기. + 방문가능한지 확인하기.
                queue.append((nextX, nextY))
                graph[nextX][nextY] = graph[x][y] + 1
            
print(graph[N-1][M-1])
    