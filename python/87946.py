# 백트래킹 방식과 순열 사용방식 두가지 존재. 우선 순열 방식으로 풀어보기.
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    dungeons = list(permutations(dungeons, len(dungeons)))
    
    for i in dungeons:
        hp = k
        count = 0
        
        for j in i:
            if j[0] <= hp:
                hp -= j[1]
                count += 1
        
        if answer < count:
            answer = count
    
    return answer