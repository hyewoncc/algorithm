"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

약수가 홀수 = 정수 제곱근을 가짐을 이용 
"""

def solution(left, right):
    answer = 0
    
    for x in range(left, right+1):
        if int(x ** 0.5) == x ** 0.5:
            answer -= x
        else:
            answer += x
            
    return answer
  
