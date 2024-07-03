from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for i in range(bridge_length)]) #다리
    truck_weights = deque(truck_weights)
    totalCount = len(truck_weights) # 전체 트럭의 개수
    totalTime = 0 #경과된 시간
    
    bridgeWeight = 0
    
    while totalCount > 0: #모든 트럭이 건널때 종료
        totalTime = totalTime + 1
        
        if bridge[-1] != 0:
            # 다리에서 빠져나가는 로직
            bridgeWeight = bridgeWeight - bridge[-1]
            bridge[-1] = 0 # 빈칸으로 바꾼 후
            totalCount = totalCount - 1
                
        bridge.rotate(1) # 다리 돌리기
        
        if truck_weights and bridgeWeight + truck_weights[0] <= weight and bridge[0] == 0: 
            # 트럭이 들어갈 수 있을 때
            bridge[0] = truck_weights.popleft()
            bridgeWeight = bridgeWeight + bridge[0]
            
    return totalTime