def solution(answers):
    # 패턴
    first = [1,2,3,4,5]
    sec = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0, 0, 0] #각 수포자의 점수
    
    for i, v in enumerate(answers):
        if first[i%len(first)] == v:
            score[0] += 1
        
        if sec[i%len(sec)] == v:
            score[1] += 1
        
        if third[i%len(third)] == v:
            score[2] += 1
    
    #각 점수 비교해서 반환값 만들기
    answer = []
    
    maxScore = max(score)
    for i, v in enumerate(score):
        if v == maxScore:
            answer.append(i+1)
    
    return sorted(answer)