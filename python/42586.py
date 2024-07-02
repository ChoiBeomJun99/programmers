def solution(progresses, speeds):
    answer = []
    # 1. 각 작업 당 배포까지 필요한 날을 구하기
    needDays = []
    
    for i, v in enumerate(progresses):
        # i == index, v == value
        tmp = v
        days = 0
        while tmp < 100:
            tmp = tmp + speeds[i]
            days = days + 1
        
        needDays.append(days)

    # 2. 일당 배포하는 기능 개수 구하기
    tmp = [] #list
    for i in needDays:
        if tmp and max(tmp) < i:
            answer.append(len(tmp))
            tmp.clear()
        
        tmp.append(i)
    
    answer.append(len(tmp))
    return answer