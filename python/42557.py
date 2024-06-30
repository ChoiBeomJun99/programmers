# 정렬 방식 이용
def solution(phone_book):
    phone_book.sort() #오름차순 정렬 
    
    # 단순 포함 여부만 체크하는 것이 아닌 접두어임을 확인해야한다.
    for i in range(len(phone_book)-1):
        tmp = phone_book[i+1][:len(phone_book[i])]
        if phone_book[i] == tmp:
            return False

    # 끝까지 접두어가 발견되지 않음.
    return True

def solution(phone_book):
    #해시를 이용한 풀이방법
    hashMap = {}
    
    for i in phone_book:
        hashMap[i] = 1
    
    for phone in phone_book:
        tmp = ""
        
        for num in phone:
            tmp += num
            if tmp in hashMap and tmp != phone:
                return False
    
    return True