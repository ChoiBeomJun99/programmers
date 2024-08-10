# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

mo = ['a','e','i','o','u'] # 모음 리스트.

while True:
    password = input().rstrip() # 우측 공백제거
    
    if password == "end": # 종료조건
        break
    
    flag = False # flag 값
    
    # 1. 모음 여부 확인하기
    for i in mo:
        if i in password:
            flag = True
            break
        
    if flag:        
        for i, v in enumerate(password):
        
            if flag and i > 1 and v in mo: #3개 연속 모음 확인 하기.
                if password[i-1] in mo and password[i-2] in mo:
                    flag = False
                
            if flag and i > 1 and v not in mo: #3개 연속 자음 확인 하기.
                if password[i-1] not in mo and password[i-2] not in mo:
                    flag = False
                
            if flag and i > 0 and password[i-1] == v: # 같은 글자가 연속적으로 두 번 발생 여부 확인(ee, oo 예외)
                if v not in ['e' , 'o']:
                    flag = False
            
    if flag:
        #예외 케이스를 통과하면 적합 
        print(f'<{password}> is acceptable.')
    else: 
        print(f'<{password}> is not acceptable.')
        
        
     