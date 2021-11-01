"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42888

조건에 따라 문자열 생성하기  
딕셔너리 자료형을 쓰는 게 포인트 였던 듯 
""" 

def solution(record):
    nickname = {}
    history = []
    
    for r in record:
        event = r.split()
        if len(event) > 2:
            nickname[event[1]] = event[2]
        if event[0] != "Change":
            history.append(event[0] + " " + event[1])
    
    for i in range(len(history)):
        s = ""
        event = history[i].split()
        s += nickname[event[1]] + "님이 "
        if event[0] == "Enter":
            s += "들어왔습니다."
        else:
            s += "나갔습니다."
        history[i] = s
        
    return history
