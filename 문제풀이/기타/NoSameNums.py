"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12906

리스트에서 연속되는 숫자만 제거하기  
지시대로 구현  
효율성 제약이 있으므로 O(n)로 만듦  
"""

def solution(arr):
    answer = [arr[0]]

    for n in arr[1:]:
        if n != answer[-1]:
            answer.append(n)
    
    return answer
