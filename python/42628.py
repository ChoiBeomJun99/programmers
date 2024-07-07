import heapq

def solution(operations):    
    heapMax = [] # 파이썬의 기본 우선순위 큐는 최대. (heap[0] == 최소값)
    heapMin = [] # 최대 우선순위 큐도 구현이 필요하다. -> -를 붙여 구현하면 된다.
    heapFlag = 0
    
    for i in operations:
        oper, value = i.split(" ")
        value = int(value)
        
        if oper == "I":
            heapq.heappush(heapMax, value)
            heapq.heappush(heapMin, (-value, value))
            heapFlag += 1
            
        elif oper == "D" and value == 1:
            if heapFlag > 0:
                heapq.heappop(heapMin) #최대값 지우기
                heapFlag -= 1
                
            
        elif oper == "D" and value == -1:
            if heapFlag > 0:
                heapq.heappop(heapMax) #최소값 지우기
                heapFlag -= 1
                
    if heapFlag == 0:
        return [0, 0]
    else:
        answer = list()
        
        # 두 리스트를 비교해서 둘 다 있으면, answer list에 넣는다.
        for i in heapMin:
            if i[1] in heapMax:
                answer.append(i[1])
                
        for i in heapMax:
            if i in [j[1] for j in heapMin]:
                answer.append(i)
                
        return [max(answer), min(answer)]