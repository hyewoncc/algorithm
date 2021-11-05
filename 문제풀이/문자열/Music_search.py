"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/17683

#이 붙은 키를 소문자로 치환하는 등 글자수에 맞춰 변형하는 게 핵심 
나머지는 특별히 어려운 게 없었으나... 
1. '(None)'을 출력해야 한다는 조건을 제대로 읽지 않았다  
2. 해당 곡이 여러 곡 있을 때, 길이를 비교하는 부분에서 논리적 오류가 있었다  
"""

def solution(m, musicinfos):
    dic = {}
    key = 1
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for music in musicinfos:
        info = music.lstrip("\"").rstrip("\"").split(",")
        start = info[0]
        end = info[1]
        info[3] = info[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        
        if start[:2] == end[:2]:
            time = int(end[3:]) - int(start[3:])
        else:
            time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
            
        if time <= len(info[3]):
            codes = info[3][:time]
        else:
            codes = info[3] * int(time//len(info[3])) + info[3][:time%len(info[3])]
            
        if m in codes:
            dic[key] = [info[2], time]
            key += 1

    if len(dic) == 0:
        return "(None)"
    else:
        answer = dic[1][0]
        flag = 1
        for k in dic.keys():
            if dic[k][1] > dic[flag][1]:
                answer = dic[k][0]
                flag = k

    return answer
