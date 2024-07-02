from itertools import combinations

array = [int(input()) for _ in range(9)]

temp = list(combinations(array, 7))

for case in temp:
    if sum(case) == 100:
        for i in sorted(list(case)):
            print(i)
        break