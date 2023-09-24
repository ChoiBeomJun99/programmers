def solution(s):
    total = 0
    countZero = 0
    while s != '1':
        tmp = s.count('0')
        countZero += tmp
        
        s = bin(len(s) - tmp)[2:]
        total += 1
        
    answer = [total, countZero]
    return answer