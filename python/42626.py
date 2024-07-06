import heapq
# heappop(x)
# heappush(x)
# heapify(x)

def solution(scoville, K):
    answer = 0
    
    # heap에 넣기
    # for i in scoville:
    #     heapq.heappush(heap, i)
    
    heapq.heapify(scoville) #해당 리스트를 바로 heap으로 변경
        
    while len(scoville) > 1 and scoville[0] < K:
        
        tmp = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, tmp) #힙에 넣기
        
        answer = answer + 1
        
        if K <= scoville[0]:
            return answer
    
    if scoville[0] >= K:
        return answer
    else:
        return -1