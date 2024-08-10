# 팩토리얼 값을 실제로 구하는 것은 아마 길이 초과
# 끝자리에 0이 있다는 것은 인수로 10의 개수를 구하는 것, 10을 만들 수 있는 소수는 5와 2, 5의 몇 제곱인지, 2의 몇제곱인지 중 작은 거를 구하면 됨.

T = int(input())
for i in range(T):
    cnt_5 = 0 # 5의 제곱수 개수
    cnt_2 = 0 # 2의 제곱수 개수

    num = int(input()) 
    tmp = num
    
    # 1. 5의 제곱수 몇인지 구하기
    insu = 5
    while tmp >= insu:
        cnt_5 += tmp // insu
        insu *= 5

    # 2. 2의 제곱수 몇인지 구하기        
    insu = 2
    while num >= insu:
        cnt_2 += num // insu
        insu *= 2
        
    print(min([cnt_5, cnt_2]))