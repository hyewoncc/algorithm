"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/42862

배열의 인덱스를 학생 번호라 생각하고 
체육복이 없는 사람 0, 하나 있는 사람 1, 여분이 있는 사람 2의 값을 넣고 처리  
무조건 앞번호 사람이 우선해서 빌려준다 가정  
지문대로 구현했는데 다른 사람들 풀이를 보니 많이 지저분한 듯...
"""

def solution(n, lost, reserve):
    students = [1] * n

    for l in lost:
        students[l-1] -= 1

    for r in reserve:
        students[r-1] += 1

    for i in range(len(students)):
        if i == 0 :
            if students[i] == 0 and students[i + 1] == 2:
                students[i + 1] -= 1
                students[i] += 1

        elif i == (len(students) - 1):
            if students[i] == 0 and students[i - 1] == 2:
                students[i - 1] -= 1
                students[i] += 1

        else:
            if students[i] == 0:
                if students[i-1] == 2:
                    students[i-1] -= 1
                    students[i] += 1

                elif students[i+1] == 2:
                    students[i+1] -= 1
                    students[i] += 1

    return students.count(1) + students.count(2)
  
  
