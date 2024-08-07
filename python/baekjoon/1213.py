# 팰린드롬 == 똑바로, 거꾸로해도 같은 문자
# 팰린드롬을 만들 수 있는 각 경우 
# 1. 각 알파벳의 개수가 홀수인것이 2개이상 가지고 있으면 안된다. -> dictionary 이용

import collections
import sys

word = sys.stdin.readline().rstrip() # 입력을 받는다.
wordCount = collections.Counter(word) # 각 알파벳의 개수를 파악한다.

oddCount = 0 #홀수의 개수
mid = '' #개수가 홀수인 알파벳이 한개일 때 이를 이용한다.

for key, value in wordCount.items():
    if value % 2 != 0: #홀수이다.
        oddCount += 1
        mid = key
        
        if oddCount > 1:
            print("I'm Sorry Hansoo")
            exit()

left = ''

for key, value in sorted(wordCount.items()):
    left += (key * (value//2))

print(left + mid + left[::-1])
    




# oddCount = 0 # 홀수의 개수
# mid = ''
# for k, v in list(wordCount.items()):
#     if v % 2 == 1: #홀수라면
#         oddCount += 1
#         mid = k #중간에 들어갈 값으로 저장 (key를 저장)
        
#         if oddCount >= 2: #홀수가 2개이상이면 펠린드롬이 불가하다
#             print("I'm Sorry Hansoo")
#             exit()

# result = ''
# for k, v in sorted(wordCount.items()): #정렬을 통해 사전순으로 for문을 돌게함
#     result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
# print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력