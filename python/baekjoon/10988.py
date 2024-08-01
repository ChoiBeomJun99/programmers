S = input()

tmp = list(S)
tmp.reverse()
tmp = "".join(tmp)

if S == tmp:
    print(1)
else:
    print(0)