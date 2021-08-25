"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/68644 

요구사항 그대로
중복 제외를 위해 set 사용  
"""

def solution(numbers):
  sum_set = {}
  for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      sum_set[numbers[i] + numbers[j]] = ""
  answer = list(sum_set.keys())  
  answer.sort()
  return answer

