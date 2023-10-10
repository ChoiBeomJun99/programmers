def solution(msg):
    answer = []
    wordDict = dict()
    lenDict = 0
    
    msg += "0"
    
    # 사전 정의하기
    for i in range(65, 91):
        lenDict += 1
        wordDict[chr(i)] = lenDict
    
    idx = 0
    while True:
        finishFlag = False
        
        for j in range(0, len(msg)):
            now = msg[idx: idx + j + 1]
            prev = msg[idx: idx + j]
            
            if "0" in now:
                finishFlag = True
            
            if now not in wordDict:
                lenDict += 1
                wordDict[now] = lenDict
                answer.append(wordDict[prev])
            
                idx += j
                break
            
        if finishFlag:
            break
        
    return answer