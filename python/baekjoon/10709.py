H, W = map(int, input().split())

answers = []

for i in range(H):
    status = input() # 현상태 확인
    answer = ""
    
    # '.' 구름이 없는 경우, 'c' 구름이 있는 경우
    # 내 가장 가까운 구름의 위치를 나타내는 상태값
    nearCloud = -1 # -1은 없다는 것.
    for index, sky in enumerate(status):
        if sky == 'c':
            answer += "0 "
            nearCloud = index
            
        else: #구름이 없는 경우 저장
            if nearCloud == -1:
                answer += "-1 "    
            else:
                answer += str(index - nearCloud) + " "
    answers.append(answer)
            
for answer in answers:
    print(answer.rstrip())
