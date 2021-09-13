"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42747

제시된 개념 이해를 제대로 못 해 오래 걸린 케이스
위키에 개념 찾아 보라는 말 듣고 해결함 -> 모르는 개념 나오면 검색 해 볼 것 
"""

def solution(citations):
    n = len(citations)
    citations.sort()

    for i in range(n):
        if n - i <= citations[i]:
            break
            
    if n - i == 1:
        return 0
    else:
        return n - i
      
