def solution(array, commands):
    answer = []
    for start, end, idx in commands:
        tmp = sorted(array[start-1:end])
        answer.append(tmp[idx-1])
    return answer