# 알파벳은 총 26개 A서부터 목표 알파벳으로 넘기는 최소 개수를 구하는 함수.
def moveCount(alpha):
    # 알파벳의 중심 n 
    if ord(alpha) < ord('N'):
        return ord(alpha) - ord('A')
    else:
        return ord('A') - ord(alpha) + 26

def solution(name):
    answer = 0
    base = ord('A')
    complete = [] # 작업이 완료된 알파벳 자리
    
    # 상하 이동(A-Z)
    for i in name:
        answer += moveCount(i)
    
    # 좌우 이동 판단하기
    min_move = len(name) - 1
    for i, char in enumerate(name):    
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        nextIdx = i + 1
        while nextIdx < len(name) and name[nextIdx] == 'A':
            nextIdx += 1
        
        min_move = min([min_move, 2 * i + len(name) - nextIdx, i + 2 * (len(name) - nextIdx)])

            
    return answer + min_move