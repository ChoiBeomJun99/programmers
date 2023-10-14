def solution(n, wires):
    answer = n
    wires.sort()
    
    # 하나씩 삭제해보며 길이를 재야한다.
    for i in range(n - 1):
        sub = [v for idx, v in enumerate(wires) if idx != i]
        
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]  
        answer = min(answer, abs(2 * len(s) - n))
        
    return answer