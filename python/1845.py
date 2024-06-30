
def solution(nums):
    N = len(nums)
    typeCount = {} # key: 포켓몬 타입, value: 해당 종류의 개체 수
    
    for pocket in nums:
        # 이미 카운트 된 이력이 있는 종류라면
        if pocket in typeCount:
            typeCount[pocket] = typeCount[pocket] + 1
        
        # 만약 한 번도 카운트 되지 않은 종류라면
        else:
            typeCount[pocket] = 1
            
    if (N / 2) <= len(typeCount):
        return N/2
    else:
        return len(typeCount)