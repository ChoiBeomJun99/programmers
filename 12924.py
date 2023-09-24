def solution(n):
    answer = 0
    
    # 연속한 자연수로 더하는 모든 경우의 수 구하기
    for i in range(1, n+1):
        tmp = 0
        
        while tmp < n:
            tmp += i
            i += 1
        
        if tmp == n:
            answer += 1
    
    return answer