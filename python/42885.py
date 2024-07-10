from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while len(people) > 1:
        if people[-1] + people[0] <= limit:
            people.popleft()
            people.pop()
        else:
            people.pop()
        
        answer += 1
    
    if people:
        answer += 1
    
    return answer

#2. 투포인터로 풀어보기
def solution(people, limit):
    people.sort()
    twoPeople = 0 # 두명이 한 번에 건너는 상황
     
    light = 0
    heavy = len(people) - 1
    
    while light < heavy: #투포인터 인덱스는 서로 같아지는 시점 직전에 종료
        if people[light] + people[heavy] <= limit:
            twoPeople += 1
            light += 1
        
        heavy -= 1
        
    return len(people) - twoPeople