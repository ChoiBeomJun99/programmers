N, M = map(int, input().split()) #N=스크린길이, M=바구니길이
j = int(input()) # 떨어지는 사과의 개수

left = 1 #시작 index
right = left + (M - 1)

answer = 0
case = []

for i in range(j):
    appleLoc = int(input())
    
    # 1. 오른쪽으로 이동해야 하는 경우, 2. 왼쪽으로 이동해야 하는 경우, 3. 가만히 있어도 되는 경우.
    if right < appleLoc: # 1. 오른쪽으로 이동해야 하는 경우
        move = appleLoc - right
        
        left += move
        right += move
        answer += move
        
    elif left > appleLoc: # 2. 왼쪽으로 이동해야 하는 경우
        move = left - appleLoc
        
        left -= move
        right -= move
        answer += move
        
    else: 
        # 3. 가만히 있어도 되는경우. (생략가능)
        continue
    
print(answer)