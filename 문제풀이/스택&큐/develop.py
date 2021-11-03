"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42586 

부등호 처리로 케이스 하나를 통과 못 했다 
조건 꼼꼼하게 따지기 
"""

def solution(progresses, speeds):
    answer = []
    
    while len(progresses) > 0:
        count = 0
        
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i]
        
        while True:
            if len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break
                
        if count != 0:
            answer.append(count)

    return answer
