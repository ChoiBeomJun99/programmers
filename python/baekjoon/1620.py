from sys import stdin
def input():
    return stdin.readline().rstrip()

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    monster = input()
    dict[i] = monster
    dict[monster] = i

for i in range(m):
    q = input()
    if q.isdigit():
        print(dict[int(q)])
    else:
        print(dict[q])