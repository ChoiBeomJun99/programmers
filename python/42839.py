from itertools import permutations

def isSosu(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

def solution(numbers):
    answer = []
    numbers = [i for i in numbers]
    
    #조합을 이용하여 풀기. 
    for i in range(len(numbers)):
        tmp = list(permutations(numbers, i+1))
        
        for j in tmp:
            num = int("".join(list(j)))
            if isSosu(num) and num not in answer:
                answer.append(num)

    return len(answer)