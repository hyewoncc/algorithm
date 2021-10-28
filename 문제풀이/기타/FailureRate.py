"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42889

특정 알고리즘 필요 X, 단계적인 논리를 고민해 옮기는 것이 중요 
코드부터 짜지 말고 의사코드를 짜거나, 최소 단계별 문장을 확실히 하고 구현하기
코드 길어져도 괜찮으니 효율성도 챙기기 
"""

import operator

def solution(n, stages):
    stages.sort()
    total = len(stages)
    dic = {}
    flag, pre = 0, 1

    for i in range(1, n+2):
        dic[i] = 0

    for j in range(total):
        stage = stages[j]

        if pre < stage:
            dic[pre] = dic[pre]/(total - flag)
            pre = stage
            flag = j

        dic[stage] += 1
        
    dic.pop(n+1)
    sdic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    answer = []

    for s in sdic:
        answer.append(s[0])

    return answer
  
