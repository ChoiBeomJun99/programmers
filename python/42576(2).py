def solution(participant, completion):
    # 동명이인이 존재하는 조건떄문에, 차집합으로 푸는 것은 불가능하다.
    player = {}
    
    # 딕셔너리에 추가
    for p in participant:
        if p in player:
            player[p] = player[p] + 1
        else:
            player[p] = 1
            
    # 딕셔너리에서 하나씩 제거
    for c in completion:
        player[c] = player[c] -1
            
    for i in player:
        if player[i] == 1:
            return i
    