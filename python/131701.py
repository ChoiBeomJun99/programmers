def solution(elements):
    answer = 0
    numberSet = set()
    
    long = len(elements)
    elements *= 2
    
    for i in range(1, long+1): # 부분 수열의 개수
        for j in range(0, long):
            numberSet.add(sum(elements[j: j+i]))
            
    answer = len(numberSet)
    return answer