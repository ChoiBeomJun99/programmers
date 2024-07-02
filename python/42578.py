def solution(clothes):
    closet = {} # 사전 생성
    
    for name, category in clothes:
        if category in closet:
            closet[category].append(name)
        else:
            closet[category] = [name]
    
    result = 1
    for i in closet:
        result = result * (len(closet[i]) + 1)
            
    return result - 1