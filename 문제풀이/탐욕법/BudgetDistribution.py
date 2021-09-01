"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12982

예산 리스트를 오름차순으로 정렬 후, 전체 예산을 초과할 때 까지 부서 수 증가  
탐욕법으로 최적해를 구할 수 있는 문제  
"""

def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    
    for x in d:
        total += x
        if budget < total:
            break
        else:
            answer += 1

    return answer
  
