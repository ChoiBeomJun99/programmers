from collections import Counter

N, C = map(int, input().split())
numbers = [int(i) for i in input().split()]

tmp = Counter(numbers) # dict형태
sortTmp = sorted(tmp.items(), key=lambda x: x[1], reverse=True)

answer = ""
for key, value in sortTmp:
    answer += (str(key) + " ") * value
    
print(answer.rstrip())