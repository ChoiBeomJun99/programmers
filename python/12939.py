def solution(s):
    answer = ''

    tmp = s.split(" ")
    tmp = [int(i) for i in tmp]
    
    answer += str(min(tmp))
    answer += " "
    answer += str(max(tmp))
    
    return answer
