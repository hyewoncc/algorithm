"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

그냥 지문대로 정직하게 만들기
정규표현식을 쓰면 더 깔끔하게 할 수 있었다
"""

def solution(input_id):
    new_id = input_id.lower()

    for x in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(x, "")

    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    if new_id == "":
        new_id = "a"

    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]

    if len(new_id) == 2:
        new_id += new_id[-1]
    elif len(new_id) == 1:
        new_id = new_id + new_id + new_id

    return new_id
  
  
