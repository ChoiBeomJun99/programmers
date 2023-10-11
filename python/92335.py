import math

def isSosu(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True
    

def solution(n, k):
    answer = 0
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    
    rev_base = rev_base[::-1] # n진수로 변경한 결과이다.
    
    while '0' in rev_base:
        idx = rev_base.find('0')
        
        if idx == 0: # 0은 계속해서 제거하기
            rev_base = rev_base[1:]
            continue
        
        check = rev_base[0:idx] # 0직전까지의 값을 저장한다.
        
        # 소수 확인 int(check)
        if isSosu(int(check)):
            # 여러 조건 체크하기
            answer += 1
            
        rev_base = rev_base[idx+1:]
        
    if rev_base and isSosu(int(rev_base)):
        answer += 1
    
    return answer