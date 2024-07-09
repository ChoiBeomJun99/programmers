#자신을 포함해서 뒤에 있는 수의 개수가 [len(number)-k] 보다는 같거나 많아야한다.
#그 중에 최대 값을 찾아야한다.


#1. 반복문과 슬라이싱으로만 푸는 풀이법. (시간초과)
def solution(number, k):
    answer = ''
    pickCount = len(number) - k #뽑아야하는 수 (0이 될때까지 계속 뽑는다.)    
    
    while pickCount > 0:
        tmp = number[:len(number)-pickCount+1] #가장 앞자리 수 중 큰 수를 골라야한다.
        
        maxValue = max(tmp)
        answer += maxValue
        maxIdx = number.index(maxValue)
        pickCount -= 1
        
        number = number[maxIdx+1:]
        
    return answer

#2.스택을 활용하기
def solution(number, k):
    stack = []
    length = len(number) - k
    
    for num in number:
        if k > 0:
            while stack and stack[-1] < num and k > 0:
                stack.pop() # 수를 빼는 것.
                k -= 1
        stack.append(num)
        
    return "".join(stack[:length])