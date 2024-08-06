N = int(input()) #재료의 개수
M = int(input()) #갑옷을 만드는데 필요한 숫자

ingredients = list(map(int,input().split())) #각 재료의 숫자
ingredients.sort() #오름차순 정렬

answer = 0

# 투포인터 사용 문제 
start, end = 0, N-1

while start < end:
    now = ingredients[start] + ingredients[end]
    
    if M == now:
        answer += 1
        start += 1
        end -= 1
        
    elif M > now: #작을경우 start += 1
        start += 1

    elif M < now: #클경우 end -= 1
        end -= 1
        
        
print(answer)