N = int(input())
numbers = [] # 숫자들이 들어가는 List

for i in range(N):
    tmp = input() #입력 받은 문자열
    number = []
    
    for j in tmp:
        if j.isdigit():
            number.append(j)
            
        else:
            if number:
                numbers.append(int("".join(number))) # 넣기전에 앞에 0은 삭제해줘야함
                number.clear()
                    
    if number:
        numbers.append(int("".join(number)))

for i in sorted(numbers):
    print(i)
    