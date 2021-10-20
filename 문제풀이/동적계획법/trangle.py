"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/43105  

동적계획법을 이용해 배열 마지막 요소의 모든 수에 대해 최선의 루트 구하고,  
그 중의 최댓값을 선택하기  
"""

def solution(triangle):
    n = len(triangle)
    values = [0] * n
    roots = [0] * n

    for row in triangle:
        for i in range(len(row)):
            if i == 0:
                roots[i] = values[i] + row[i]
            elif i == len(row)-1:
                roots[i] = values[i-1] + row[i]
            else:
                if values[i-1] > values[i]:
                    roots[i] = values[i-1] + row[i]
                else:
                    roots[i] = values[i] + row[i]
        values = roots.copy()

    answer = max(values)
    return answer
