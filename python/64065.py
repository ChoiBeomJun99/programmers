def solution(s):
    answer = []
    s = s[1:-1] # 앞뒤 '{' 와 '}' 삭제해주기
    collectionList = s.split('},')
    collectionList = sorted(collectionList, key = lambda x:(len(x)))

    for i, v in enumerate(collectionList):
        tmp = v[1:]
        if v[-1] == '}':
            tmp = v[1:-1]
            
        tmp = tmp.split(',')
        for j in tmp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer