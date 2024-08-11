# 브루트 포스이다...
N = int(input()) # 6이 적어도 3개 연속으로 들어가는 수 중 N번째의 수를 리턴한다.

tmp = 666
cnt = 0

while True:
    if '666' in str(tmp):
       cnt += 1 
    
    if N == cnt:
        print(str(tmp))
        break
    
    tmp += 1