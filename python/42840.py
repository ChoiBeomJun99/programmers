# 각 규칙 정의
pattern = ['12345', '21232425', '3311224455']

def solution(answers):
    score = []
    
    for i in range(3): # 3개의 각 패턴으로 검사하기
        count = 0
        
        tmp = (pattern[i] * (len(answers) // len(pattern[i])) + (pattern[i][:len(answers) % len(pattern[i])]))
        
        for idx, v in enumerate(answers):
            if str(v) == tmp[idx]:
                count += 1
        
        score.append(count)
    
    tmp = max(score)
    
    answer = []
    for i, v in enumerate(score):
        if v == tmp:
            answer.append(i+1)
    
    return answer