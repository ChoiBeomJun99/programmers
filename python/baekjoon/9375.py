import sys

T = int(sys.stdin.readline().strip())

# 테스트케이스 개수만큼 반복
for _ in range(T):
    closet = {} #옷장
    n = int(sys.stdin.readline().strip()) #의상의 총개수
    
    for _ in range(n):
        name, type = sys.stdin.readline().strip().split() #종류와 이름을 나눈다.
        
        # 각 부위별 개수를 저장한다.
        if type not in closet:
            closet[type] = 1
        else: 
            closet[type] += 1

    # 의상의 종류가 1개일때            
    if len(closet) == 1:
        print(n)
        continue
            
    # dict를 순환한다.
    mul = 1
    for c in closet:
        mul *= (closet[c] + 1)
        
    print(mul-1)
