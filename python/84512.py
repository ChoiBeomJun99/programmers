from itertools import product

def solution(word):
    answer = 0
    alpha = list("AEIOU")
    
    allCase = []
    
    for i in range(1, 6):
        for j in list(product(alpha, repeat=i)):
            allCase.append("".join(j))
            
    allCase.sort()
    answer = allCase.index(word)
    
    return answer + 1