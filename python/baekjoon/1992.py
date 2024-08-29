N = int(input())

arr = []
for i in range(N):
    tmp = [int(j) for j in input()]
    arr.append(tmp)
    
answer = ''
# 1. 1/4 정사각형을 따져보면서, 모든 수가 같은 수(0이나 1)로 되어있는지 확인한다. 만약 다른 수가 있다면 재귀 실행.
def recursive(x, y, N):
    global answer # 이걸 해주어야 한다...
    standard = arr[y][x] # 정사각형 범위의 모든수가 이와 같은지 확인한다.
    size = N//2 # 확인할 정사각형의 한 변의 길이
    
    for i in range(y, y+N):
        for j in range(x, x+N):
            if arr[i][j] != standard: # 같지 않은 수가 발생하면 -> 4개의 정사각형으로 나눠야함으로
                answer += '('
                recursive(x, y, size) # 왼쪽 위
                recursive(x+size, y, size) # 오른쪽 위
                recursive(x, y+size, size) # 왼쪽 아래
                recursive(x+size, y+size, size) # 오른쪽 아래
                answer += ')'
                return
    
    # 2. 만약 다 같다면 해당 수를 집어 넣으면 된다.
    answer += str(standard)

recursive(0, 0, N) # 0, 0 부터 시작한다.    
print(answer)
