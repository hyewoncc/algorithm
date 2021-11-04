"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/64065 

lstrip, rstrip, split 을 잘 알았다면 더 깔끔하게 할 수 있었다 
시도했었는데 잘 안됐는데 방법을 더 생각해 봤으면 하는 아쉬움이 있음 
논리 자체는 괜찮았다  
"""

def solution(s):
    dic = {}
    num = ""
    key = 0
    piece = []
    answer = []
    
    for a in s:
        if a.isdigit():
            num += a
        elif a == "," and num != "":
            piece.append(int(num))
            num = ""
            key += 1
        elif a == "}" and num != "":
            key += 1
            piece.append(int(num))
            dic[key] = piece.copy()
            num = ""
            piece = []
            key = 0
    sdic = sorted(dic.items())
    
    for i in sdic:
        for j in i[1]:
            if j not in answer:
                answer.append(j)
                
    return answer

  
