def solution(numbers): 
    tmp = [str(i) for i in numbers]
    tmp.sort(key=lambda i:i*3, reverse=True)
    
    return str(int("".join(tmp)))