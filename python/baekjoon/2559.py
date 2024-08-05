import sys
input = sys.stdin.readline

n, k = map(int,input().split()) #N: 온도를 잰 날들의 개수, k:더해야하는 연속일 수 
a = list(map(int, input().split()))

now = sum(a[0:k])
max = now

for i in range(1, len(a) - k + 1):
    tmp = now - a[i-1] + a[i+k-1]
    if max < tmp:
        max = tmp
        
    now = tmp
    

print(max)