alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def translate(n, jin):
    # jin: 몇진수, n: 바꿀 숫자
    if n == 0:
        return '0'
    
    result = ''
    
    while n > 0:
        n, mod = divmod(n, jin)
        
        if mod in alpha:
            result += str(alpha[mod])
        else:
            result += str(mod)
        
    return result[::-1]
    

def solution(n, t, m, p):
    answer = ''
    
    fullList = "" # n진수를 변경한 것에 대한 모든 값을 이 변수에 저장
    for i in range(m * t):
        fullList += (translate(i, n))
    
    for i in range(p-1, m * t, m):
        answer += fullList[i]
            
    return answer