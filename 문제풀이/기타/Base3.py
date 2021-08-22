"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/68935

지문대로 정석 처리 
"""

def solution(n):
    code = []
    answer = 0

    while n > 0:
        code.append(n % 3)
        n //= 3

    for i, v in enumerate(reversed(code)):
        answer += v * (3 ** i)

    return answer
  
  
