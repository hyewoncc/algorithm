"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/1845

코드 짜기 보다 논리적 사고가 중점이라고 느껴진 문제 
파이썬에 set이 있는 줄 몰라서 딕셔너리 쓰느라 코드가 길어졌다...
"""

# 먼저 해결한 코드 
def solution1(nums):
    dic = {}

    for n in nums:
        if n in dic.keys():
            dic[n] += 1
        else:
            dic[n] = 0

    if len(dic.values()) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(dic.values())

      
# 다른 사람의 풀이에서 set을 참고해 수정한 코드
def solution2(nums):
    mons = set(nums)

    if len(mons) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(mons)
      
      
