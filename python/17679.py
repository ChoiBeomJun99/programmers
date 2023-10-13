def isDelete(m, n, board):
    tmp = board[m][n]
    
    if tmp == board[m+1][n] and tmp == board[m][n+1] and tmp == board[m+1][n+1]:
        return True
    
    return False
    

def solution(m, n, board):
    answer = 0    
    board = [list(i) for i in board] # list로 변환하기.
    
    while True:
        rmList = set() # 지워야할 목록
        
        # board에서 지워질 목록 탐색하기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] and isDelete(i, j, board):
                    rmList.add((i, j))
                    rmList.add((i, j + 1))
                    rmList.add((i + 1, j))
                    rmList.add((i + 1, j + 1))
        
        # 없다면 삭제될게 없다는 뜻이므로 break   
        if not rmList:
            break
        
        # 지우고 아래로 내리기
        answer += len(rmList)
        for i in rmList:
            board[i[0]][i[1]] = []
            
        while True:
            flag = False # 이번에 내려가는 활동을 진행하였는지 체크
            
            for i in range(m):
                for j in range(n):
                    if i + 1 < m and board[i][j] != [] and board[i+1][j] == []:
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        flag = True
            
            if not flag:
                break
                
    return answer