def solution(participant, completion):
    partDict = dict()
    
    count = 0
    for i in participant:
        partDict[hash(i)] = i
        count += hash(i)
        
    for j in completion:
        count -= hash(j)
        
    return partDict[count]