# 바이러스가 퍼져가는 과정을 계산해야 함으로, BFS 문제이다.
# 벽은 무조건 3개를 다세워야한다. 3개의 벽을 세운 모든 경우에서. 안전지대의 최댓값을 구한다. -> 백트래킹 필요
# BFS + 백트래킹 문제이다. 
# 벽은 0이라는 곳에서만 세울 수 있다.

from collections import deque
from itertools import combinations
import copy

# 입력값
N, M = map(int, input().split(" "))
graph = [[0] * M for _ in range(N)]

# 입력값대로 graph 구현하기
for x in range(N):
    tmp = input().split(" ")
    
    for y in range(M):
        graph[x][y] = int(tmp[y])
        
answer = 0 # 리턴할 정답

# 바이러스가 퍼지는 과정 (BFS 구현)
dx = [0, 0, -1, 1] #위, 아래, 왼쪽, 오른쪽
dy = [1, -1, 0, 0]

def bfs(tmp_graph):
    queue = deque()
    # tmp_graph = copy.deepcopy(graph) #이게 중요하네
    
    # queue에 바이러스들의 좌표를 넣어준다.
    for x in range(N):
        for y in range(M):
            if tmp_graph[x][y] == 2:
                queue.append((x, y))
                
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            
            # if 0 <= mx < N and 0 <= my < M and tmp_graph[mx][my] == 0:
            
            if mx < 0 or mx >= N or my < 0 or my >= M:
                continue
            
            if tmp_graph[mx][my] == 0:
                tmp_graph[mx][my] = 2 #바이러스에 감염시키기
                queue.append((mx, my))
    
    global answer
    cnt = 0
    
    #안전지대 수 세기
    for x in range(N):
        cnt += tmp_graph[x].count(0)
    
    answer = max(answer, cnt)

# 3개의 벽을 세우는 과정 (모든 경우에 대해서 백트래킹으로 수행한다.) -> 조합방식으로 대입해본다.
def createWall(wallCnt):
    if wallCnt == 3:
        bfs()
        return
    
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                graph[x][y] = 1 #벽세우기
                createWall(wallCnt + 1)
                # 여기까지 왔다는 것은 끝났다는 것
                graph[x][y] = 0 # 벽허물기
                

def createWall_combinations():
    # 1. 0인 좌표를 다 구해본다.
    isZero = []
    
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                isZero.append((x, y))
    
    combinations_isZero = list(combinations(isZero, 3))
    
    for i in combinations_isZero:
        tmp_graph = copy.deepcopy(graph) #이게 중요하네
        for j in i:
            x, y = j
            tmp_graph[x][y] = 1 #벽세우기
            
        bfs(tmp_graph)
            
# Main 부분                
# createWall(0)
createWall_combinations()
print(answer)
                
        
    