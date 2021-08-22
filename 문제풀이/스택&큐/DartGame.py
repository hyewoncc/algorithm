"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/17682

문자열 앞에서부터 문자열 큐에 담은 뒤 SDT가 오면 숫자를 꺼내서 계산 후 점수 큐에 
*#가 나오면 큐에서 점수를 꺼내서 계산 후 다시 담기 
*이고 앞의 점수가 있을 경우에는 두 개 꺼내서 처리
점수 큐 더해서 리턴
"""

from collections import deque

def solution(dartResult):
    que = deque()
    s_que = deque()

    for s in dartResult:
        if s in "0123456789":
            que.append(s)

        elif s in "SDT":
            score = ""
            while len(que) != 0:
                score += que.popleft()
            if s == "D":
                score = int(score) ** 2
            elif s == "T":
                score = int(score) ** 3
            else:
                score = int(score)
            s_que.append(score)
        else:
            if s == "*":
                if len(s_que) > 1:
                    temp = s_que.pop() * 2
                    s_que.append(s_que.pop() * 2)
                    s_que.append(temp)
                else:
                    s_que.append(s_que.pop() * 2)
            else:
                s_que.append(s_que.pop() * -1)

    return sum(s_que)
  
