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