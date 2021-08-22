"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/parts/12081

리스트를 큐로 활용, 다리 길이 만큼의 리스트와 트럭 무게가 들어있는 리스트를 만든다  
다리 큐에서 트럭이 없는 공간은 0을 채운다  
시간에 따라 다리에 올라간 무게를 계산하여 트럭 큐에서 꺼내온 트럭을 올릴지 말지 결정한다  
트럭 큐가 비고 다리 무게가 다시 0이 될 때 까지(=트럭이 다 지나갈 때 까지) 반복  

queue와 deque를 활용하려다 peek/front가 필요한 부분이 있어서 결국 리스트로 했는데...  
통과는 했으나 시간 지연이 많이 되는 테스트 케이스가 있었음  
클래스를 이용한 다른 사람의 문제 풀이 공부해볼 것  
"""

def solution(bridge_length, weight, truck_weights):
    
    bridge_que = [0] * bridge_length
    truck = 0
    time = 0
    weight_on_bridge = 0

    while True:
        if len(truck_weights) != 0 and truck == 0:
            truck = truck_weights.pop(0)

        if (weight_on_bridge + truck - bridge_que[0]) <= weight:
            weight_on_bridge -= bridge_que.pop(0)
            weight_on_bridge += truck
            bridge_que.append(truck)
            truck = 0
        else:
            weight_on_bridge -= bridge_que.pop(0)
            bridge_que.append(0)

        time += 1

        if len(truck_weights) == 0 and weight_on_bridge == 0:
            break

    return time
