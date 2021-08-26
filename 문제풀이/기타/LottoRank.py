"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/77484

생각한 대로 구현 
처음에 케이스 하나 불통과 -> 0이 없는 경우의 수 였음 
"""

def solution(lottos, win_nums):
    count = 0
    blank = 0
    
    for num in lottos:
        if num in win_nums:
            count += 1
        if num == 0:
            blank += 1
            
    return [ 6 if count == 0 and blank == 0 else 7-count-blank,
            7-count if count != 0 else 6 ]
  
