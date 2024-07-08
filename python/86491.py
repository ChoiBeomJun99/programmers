def solution(sizes):
    width = []
    height = []
    
    for i in sizes:
        w, h = i
        
        if w > h:
            width.append(w)
            height.append(h)
        else:
            width.append(h)
            height.append(w)
            
    return max(width) * max(height)