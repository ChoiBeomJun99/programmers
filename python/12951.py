def solution(s):
    answer = ''
        
    for i, v in enumerate(s):
        if i == 0 and v.isalpha():
            answer += v.upper()
        
        elif i > 0 and s[i-1] == " " and v.isalpha():
            answer += v.upper()
            
        elif v.isalpha():
            answer += v.lower()
            
        else:
            answer += v
            
    return answer