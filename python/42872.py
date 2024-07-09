def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    cf = [] # 예외 학생들
    
    # 1. 여벌 체육복을 가져온 학생이 도난 당한 경우 제외하기
    for i in reserve:
        if i in lost:
            cf.append(i)
    
    for i in cf:
        lost.remove(i)
        reserve.remove(i)
    
            
    # 2. 체육복 빌려주는 로직
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n - len(lost)