import sys
input = sys.stdin.readline

result =[]

n, k = map(int,input().split()) # 
a = list(map(int, input().split()))

answer = sum(a[0:k])
prev = answer

for i in range(1, n-k+1):
    tmp = prev - a[i-1] + a[i+k-1]
    
    if tmp > answer:
        answer = tmp
        prev = tmp
        
    else:
        prev = tmp
        
print(answer)