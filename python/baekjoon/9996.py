N = int(input())
pattern = input().split('*') #패턴을 별표 기준으로 나누기

fileName = []
for _ in range(N):
    tmp = input()
    fileName.append(tmp)

# *를 기준으로 나눈 패턴 list를 기반으로 확인한다. 별표는 무조건 중간에만 존재한다, 별표는 무조건 한개이다.
for f in fileName:
    if len(pattern[0]) + len(pattern[1]) > len(f):
        print("NE")
        continue
    
    if f[0:len(pattern[0])] == pattern[0] and f[len(f)-len(pattern[1]):] == pattern[1]:  
        print("DA")
    else:
        print("NE")