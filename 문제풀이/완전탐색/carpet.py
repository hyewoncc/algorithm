"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42842

카펫의 세로길이 x에 대해 x의 범위는 1 ~ 루트 yellow
약수라면 둘레 계산 시 brown이 나오는지 확인
"""

def solution(brown, yellow):

    for x in range(int(yellow**0.5), 0, -1):
        if yellow % x == 0 and 2*(x + yellow/x + 2) == brown:
            answer = [yellow/x+2, x+2]
    
    return answer

