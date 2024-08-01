S = input()
result = ""

#암호화 실시
for i in S:
    if i.isalpha():
        if ord(i) < ord('a'): #대문자인경우
            result += chr(ord('A') + ((ord(i) + 13 - ord('A')) % 26))
        else: #소문자인경우
            result += chr(ord('a') + ((ord(i) + 13 - ord('a')) % 26))
    else:
        result += i
        
print(result)