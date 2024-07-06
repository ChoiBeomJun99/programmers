def solution(prices):
    answer = []
    
    # 리스트 두 개를 가지고 비교하기.
    for i, v in enumerate(prices):
        tmp = 0
        # index: i, value: v
        for idx in range(i+1, len(prices)-1):
            if prices[idx] < v:
                tmp = 1
                answer.append(idx-i)
                break
        
        if tmp == 0:
            answer.append(len(prices)-i-1)
    
    return answer