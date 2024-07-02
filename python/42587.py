from collections import deque

def solution(priorities, location):
    orgLen = len(priorities)
    priorities = deque(priorities) #큐를 구현하기 위한 것 (시간절약)
    outProcess = 0 # 현재 실행된 프로세스 개수
    
    while len(priorities) > 1:
        tmp = priorities.popleft()
        
        if tmp >= max(priorities):
            # 큐에서 꺼낸 값이 가장 크다면 실행.
            if location == 0:
                # 내가 찾는 값이 나온 것
                return outProcess + 1
            else:
                # 내가 찾는 값이 아니면, 넣진 말고
                outProcess = outProcess + 1        
        else:
            priorities.append(tmp) #다시 큐에 넣기
            
            if location == 0:
                location = len(priorities) - 1
                continue
        
        location = location-1
    
    # 여기까지 왔다는 것은 이미 마지막까지 돌았다는 것.
    return orgLen