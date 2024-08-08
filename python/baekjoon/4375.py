# 테스트 케이스의 개수가 없다. 
while True: 
    try:
        n = int(input())
    except:
        break

    start = 1
    while start % n != 0: # n의 배수인경우 종료
        # start = int(str(start) + "1") //문자열로 처리하는 방법 *시간초과
        start = start * 10 + 1 
        
    print(len(str(start)))