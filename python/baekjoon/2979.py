a,b,c = map(int,input().split()) # 주차요금가격

maxTime = 0
timeArray = [] #시작과 종료시간을 담는 트럭 len=3
# 각 트럭의 시작시간과 나가는 시간
for _ in range(3):
    start, end = map(int, input().split())
    timeArray.append([start, end])
    
    if end > maxTime:
        maxTime = end
    
total = 0 # 답: 총 요금
state = [0 for i in range(maxTime)] # 각 초당 존재하는 트럭의 개수 (index는 초를 나타낸다.)

for start, end in timeArray:
    for j in range(start-1, end-1):
        state[j] += 1
        
for i in state:
    if i == 3:
        total += (c*3)
    elif i == 2:
        total += (b*2)
    elif i == 1:
        total += a

# print(state)
print(total)