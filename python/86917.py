def solution(n, wires):
    answer = n
    wires.sort()
    
    # 하나씩 삭제해보며 길이를 재야한다.
    for i in range(n - 1):
        sub = [v for idx, v in enumerate(wires) if idx != i]
        
        s = set(sub[0])
        for j in range(len(sub)):
            for k in sub:
                if set(v) & k:
                    s.update(k)
        answer = min(answer, abs(2 * len(s) - n))
        
    return answer