def solution(arr):
    queue = []
    
    for i in arr:
        if not queue or i != queue[-1]:
            queue.append(i)
    
    return queue