"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

프린트 할 문서 리스트를 deque로 생성하고, 
길이가 같은 다른 deque에 location번째는 1, 나머지는 모두 0 값 저장
값을 하나씩 뽑으면서 제일 크면 제거 후 내 목표 문서였는지 확인 
제일 큰 수가 아니라면 마지막에 추가하기를 반복 
"""

from collections import deque


def solution(priorities, location):
    documents_que = deque(priorities)
    target_que = deque()
    count = 0

    for i in range(len(priorities)):
        if i == location:
            target_que.append(1)
        else:
            target_que.append(0)

    while True:
        printing = True
        index = target_que.popleft()
        select = documents_que.popleft()
        for document in documents_que:
            if select < document:
                printing = False
                break

        if not printing:
            target_que.append(index)
            documents_que.append(select)
        else:
            count += 1
            if index == 1:
                return count
              
