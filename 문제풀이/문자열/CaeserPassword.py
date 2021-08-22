"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12926

문제대로 구현
string += 연산 대신 list에 append후 join 하는 게 나은 걸 주의 
"""

def solution(s, n):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    answer = ""

    for x in s:
        if x.isspace():
            answer += x
        else:
            if x.isupper():
                answer += uppers[(uppers.index(x) + n)%26]
            else:
                answer += lowers[(lowers.index(x) + n)%26]

    return answer
  
