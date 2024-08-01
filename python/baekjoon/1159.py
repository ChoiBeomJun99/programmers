n = int(input()) # 후보선수 수

alpha = [0 for i in range(26)] #각 알파벳으로 시작하는 선수 개수를 나타내는 배열
for _ in range(n):
    a = input()
    alpha[ord(a[0]) - ord('a')] += 1
    
result = ""
for i, v in enumerate(alpha):
    if v >= 5:
        result += chr(i + ord('a'))

if len(result) > 0:
    print(result) # 정답출력
else:
    print("PREDAJA") # 항복