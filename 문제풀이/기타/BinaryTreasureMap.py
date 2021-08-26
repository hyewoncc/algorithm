""" 
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/17681

지문대로 구현 
"""

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line1 = format(arr1[i], 'b')
        line1 = (n-len(line1)) * "0" + line1
        line2 = format(arr2[i], 'b')
        line2 = (n-len(line2)) * "0" + line2
        answer_line = ""
        for j in range(n):
            if line1[j] == "0" and line2[j] == "0":
                answer_line += " "
            else:
                answer_line += "#"
        answer.append(answer_line)

    return answer

 
