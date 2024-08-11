N = int(input())

time = [0, 0]
score = [0, 0]
 
tmp = 0 #분, 초 중요시점 기록
state = 0 # 0: 비기는 상황, 1: 1이 이기는 상황, 2: 2가 이기는 상황
for i in range(N):
    team, nowTime = input().split(" ")
    nowTime = [int(j) for j in nowTime.split(':')] # 0: min, 1:sec
    nowTime = nowTime[0] * 60 + nowTime[1] # 분으로 수정하기
    
    score[int(team) - 1] += 1
    
    # 어느 팀이 이기는 순간보다. 1) 비기게 되는 순간 2) 경기가 끝난 순간
    if score[0] > score[1] and state == 0: #비기고 있다가 팀1이 이기게 된 순간(기록 필요)
        tmp = nowTime
        state = 1
    elif score[1] > score[0] and state == 0: #비기고 있다가 팀2가 이기게 된 순간(기록 필요)
        tmp = nowTime
        state = 2
    elif score[0] == score[1]: # 비기게 된 순간 (누군가의 이기고 있던 시간을 갱신)
        if state == 1: # 1이 이기고 있던 상황
            time[0] += (nowTime - tmp)
        elif state == 2: # 2가 이기고 있던 상황
            time[1] += (nowTime - tmp)
        state = 0

#2) 경기가 끝난 순간 확인하기 / 비겼을 시는 계산 안하기.
if state == 1: 
    time[0] += (48 * 60 - tmp)
elif state == 2:
    time[1] += (48 * 60 - tmp)
    
print("{:0>2}:{:0>2}".format(time[0] // 60, time[0] % 60))
print("{:0>2}:{:0>2}".format(time[1] // 60, time[1] % 60))
