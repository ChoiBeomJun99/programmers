from collections import deque

M, N, K = map(int, input().split(" ")) # 입력값
graph = [[0] * N for i in range(M)] # 그래프

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split(" "))
    
    for x in range(x1, x2): #그래프에 직사각형이 칠해진 곳을 표시하는 과정
        for y in range(M-y2, M-y1):
            graph[y][x] = 1
            
dx = [0, 0, 1, -1] #위, 아래, 왼쪽, 오른쪽 순서
dy = [1 ,-1, 0 ,0]

answer = []

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    graph[y][x] = 1
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            if 0 <= mx < N and 0 <= my < M and graph[my][mx] == 0:
                graph[my][mx] = 1
                queue.append((mx, my))
                cnt += 1
    
    answer.append(cnt)

for y in range(M):
    for x in range(N):
        if graph[y][x] == 0:
            bfs(x, y)

print(len(answer))
for i in sorted(answer):
    print(i, end=' ')
        
    