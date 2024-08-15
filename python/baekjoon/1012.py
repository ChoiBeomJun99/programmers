from collections import deque

T = int(input()) #테스트 케이스 개수

for _ in range(T):
    answer = 0
    M, N, K = map(int, input().split(" "))
    
    # 위, 아래, 왼쪽, 오른쪽
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split(" "))
        graph[y][x] = 1 # 배추
        
    # 상하좌우로 이동할 수 있는 지역 그룹을 세야한다.
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        graph[y][x] = 0 #방문했으므로
        
        while queue:
            x, y = queue.popleft()
            
            for j in range(4):
                mx = x + dx[j]
                my = y + dy[j]
                
                if 0 <= mx < M and 0 <= my < N and graph[my][mx] == 1:
                    queue.append((mx, my)) #queue에 넣기
                    graph[my][mx] = 0
                
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                bfs(x, y)
                answer += 1
                
    print(answer)
                
    