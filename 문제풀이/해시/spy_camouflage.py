"""
프로그래머스 - 위장
https://programmers.co.kr/learn/courses/30/lessons/42578

딕셔너리를 이용해 옷 부위별 가짓수를 입지 않았을 때를 더해 구한 후,  
아무것도 입지 않는 경우의 수인 하나를 빼 준다 
"""

def solution(clothes):
    answer = 1
    
    # 부위별 가짓수를 담을 딕셔너리
    dic_clothes = {}
    
    # 리스트를 순회하며 부위별 가짓수를 계산 
    # 입지 않았을 때를 포함하기 위해 처음 나타나면 2로 처리 
    for cloth in clothes:
        if cloth[1] not in dic_clothes:
            dic_clothes[cloth[1]] = 2
        else:
            dic_clothes[cloth[1]] += 1
    
    # 딕셔너리를 순회하며 가짓수를 곱한다 
    for cloth in dic_clothes:
        answer *= (dic_clothes[cloth])
    
    # 모든 부위에 아무것도 입지 않았을 때를 빼주면서 리턴 
    return answer - 1
  
