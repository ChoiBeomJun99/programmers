# 입력값의 길이는 9, 이중 7개를 뽑았을때 합이 100이 되어야한다. 
# 조합을 사용한다면, 이는 높은 시간복잡도를 가질 수 있음.
# from itertools import combinations

# array = []
# for i in range(9):
#     array.append(int(input()))
    
# allCase = list(combinations(array, 7))

# for i in allCase:
#     if sum(i) == 100:
#         for j in sorted(i):
#             print(j)
#         break
    
    
# 재귀 이용 방법(DFS)
array = [int(input()) for _ in range(9)] # 입력값 받아오기
seven_short_temp = []  # 7명을 뽑아 합을 조사할 새로운 리스트 선언

def dfs(depth, start):
    if depth == 7:  # 7번을 시행했다면. (7개의 수를 다 담았다면.)
        if sum(seven_short_temp) == 100:  # 현재 저장된 일곱난쟁이들의 합이 100이라면
            for j in sorted(seven_short_temp):  # 오름차순으로 정렬 후 출력
                print(j)
            exit()  # 그 후 코드 종료
        else:  # 만약 7명을 뽑았는데 합이 100이 아니라면
            return  # 해당 재귀를 더이상 실행하지 않고 종료
        
    for i in range(start, len(array)): 
        seven_short_temp.append(array[i])
        dfs(depth + 1, i + 1)  # dfs를 돈다(다음번 깊이는 +1로 해주고 인덱스는 중복되지 않게 하기위해서 다음 인덱스를 넣어준다.)
        seven_short_temp.pop()  # dfs를 돌다 7명이 다 찼으나 합이 100이 아니어서 return 되었으면 넣었던 난쟁이 한명을 다시 빼준다.

dfs(0, 0)  # dfs를 돈다.