S = input()

answer = [0 for i in range(26)]

for i in S:
    answer[(ord(i) + 7) % 26] += 1

for i in answer:
    print(i, end=' ')