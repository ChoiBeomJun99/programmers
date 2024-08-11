def plusTime(team, time, tmp):   
   # min 계산
   result = team
   result[0] += time[0] - tmp[0]
   
   # sec 계산
   if time[1] < tmp[1]:
       result[0] -= 1
       result[1] = 60 - (tmp[1] - time[1])
   else:
       result[1] = time[1] - tmp[1]

   return result

N = int(input())

score_1, time_1 = 0, [0, 0] # 팀1의 스코어, 팀1의 이기고 있던 시간
score_2, time_2 = 0, [0, 0]# 팀2의 스코어, 팀2의 이기고 있던 시간
 
tmp = [0, 0] #분, 초 중요시점 기록

state = 0 # 0: 비기는 상황, 1: 1이 이기는 상황, 2: 2가 이기는 상황
for i in range(N):
    team, time = input().split(" ")
    time = [int(j) for j in time.split(':')] # 0: min, 1:sec
    
    # 골을 추가해주기
    if team == '1':
        score_1 += 1
    else: 
        score_2 += 1

    # 어느 팀이 이기는 순간보다. 1) 비기게 되는 순간 2) 경기가 끝난 순간
    if score_1 > score_2 and state == 0: #비기고 있다가 팀1이 이기게 된 순간(기록 필요)
        tmp = [time[0], time[1]]
        state = 1
    elif score_2 > score_1 and state == 0: #비기고 있다가 팀2가 이기게 된 순간(기록 필요)
        tmp = [time[0], time[1]]
        state = 2
    elif score_1 == score_2: # 비기게 된 순간 (누군가의 이기고 있던 시간을 갱신)
        if state == 1: # 1이 이기고 있던 상황
            time_1 = plusTime(time_1, time, tmp)
        elif state == 2: # 2가 이기고 있던 상황
            time_2 = plusTime(time_2, time, tmp)
        state = 0

#2) 경기가 끝난 순간 확인하기 / 비겼을 시는 계산 안하기.
if state == 1: 
    time_1 = plusTime(time_1, [48, 0], tmp)
elif state == 2:
    time_2 = plusTime(time_2, [48, 0], tmp)

print("{:0>2}:{:0>2}".format(time_1[0], time_1[1]))
print("{:0>2}:{:0>2}".format(time_2[0], time_2[1]))
