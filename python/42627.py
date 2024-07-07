import heapq

def solution(jobs):
    heap = [] # 현시점 실행 가능한 작업들
    executeJobsIdx = [] #실행한 작업 idx
    
    answer = 0 #답
    time = 0 # 현재 경과한 시간
    
    while len(executeJobsIdx) < len(jobs) :
        for i, v in enumerate(jobs):
            if  v[0] <= time and i not in executeJobsIdx and [v[1], v[0], i] not in heap:
                heapq.heappush(heap, [v[1], v[0], i])
        
        if heap:
            job = heapq.heappop(heap)
            time += job[0] #현재 경과한 시간 더해주기(현재 작업이 끝나는 시간)
            executeJobsIdx.append(job[2]) #실행한 작업 idx 넣어주기
            answer += (time - job[1])
            
        else:
            time = time + 1 # time+=1

    return int(answer / len(jobs))