"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/42840

어차피 시험은 최대 10000문제니까 문자열을 10000까지 뻥튀기 한 후 비교해서 풀었는데... 
다른 사람들 코드를 보니 역시 패턴화가 정석적으로 맞는 것 같다
생각을 게으르게 한 건 아닌가 하면서도 쉬운 방법을 두고 굳이? 싶기도 하고...
"""

def solution(s):
    a1 = "12345"*2000
    a2 = "21232425"*1250
    a3 = "3311224455"*1000
    score = [0, 0, 0]
    answer = []
    
    for i in range(len(s)):
        if s[i] == int(a1[i]):
            score[0] += 1
        if s[i] == int(a2[i]):
            score[1] += 1
        if s[i] == int(a3[i]):
            score[2] += 1
            
    for j in range(3):
        if score[j] == max(score):
            answer.append(j+1)
    
    return answer
