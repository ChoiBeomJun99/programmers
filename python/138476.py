
def solution(k, tangerine):
    answer = 0
        
    typeDict = {}
    for i in tangerine:
        typeDict[i] = typeDict.get(i, 0) + 1
        
    typeList = sorted(typeDict, key = lambda x:typeDict[x], reverse = True)
        
    for i in typeList:
        k -= typeDict[i]
        answer += 1
        
        if k <= 0:
            break
        
    return answer