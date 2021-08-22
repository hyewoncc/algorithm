"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

문자열 순회하면서 공백인가/홀수번째인가/짝수번째인가 따라서 처리 후 리스트에 담고 문자열화 해서 반환해주기 
"""

def solution(s):
    index = 0
    answer = []
    
    for x in s:
        if x.isspace():
            answer.append(" ")
            index = 0
        else:
            answer.append(x.lower()) if index % 2 else answer.append(x.upper())
            index += 1
        
    return ''.join(answer)
