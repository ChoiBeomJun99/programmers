def solution(n):
    answer = 0
    tmp = n + 1
    
    while True:
        if bin(tmp).count('1') == bin(n).count('1'):
            answer = tmp
            break
    
        tmp += 1
    
    return answer