def solution(brown, yellow):
    answer = []
    
    if yellow == 1:
        return [3, 3]
    
    yellowCase = []
    # yellow 기준 서로 곱해서 yellow가 되는 수들을 구해본다.
    for i in range(1, int(yellow/2) + 1):
        if yellow % i == 0 and [i, int(yellow / i)] not in yellowCase:
            yellowCase.append([int(yellow / i), i])
    
    for i in yellowCase:
        w, h = i
        if (w + 2)*2 + (h + 2)*2 - 4 == brown :
            return [w+2, h+2]
    
    return answer