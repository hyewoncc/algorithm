"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/17677

1. 제시한 집합 개념을 제대로 이해하지 못해서 시간을 많이 끌었다
2. set을 사용하려다 중복 원소가 있어 딕셔너리 순회로 풀었는데, 
  일단 set을 사용한 후, Counter로 원소 개수를 세는 방법이 있었다 
3. 분모가 0이 되는 경우를 생각하지 못했다 
4. isalpha()가 존재함을 자꾸 까먹는다... 큰 문제는 아니라고 생각하지만 
"""

import math

def solution(str1, str2):
    alphas = "abcdefghijklmnopqrstuvwxyz"
    str1 = str1.lower()
    str2 = str2.lower()
    dic1, dic2 = {}, {}
    dic_den, dic_num = {}, {}
    den, num = 0, 0

    while len(str1) > 1:
        if str1[0] in alphas and str1[1] in alphas:
            piece = str1[:2]
            if piece not in dic1:
                dic1[piece] = 1
            else:
                dic1[piece] += 1
        str1 = str1[1:]

    while len(str2) > 1:
        if str2[0] in alphas and str2[1] in alphas:
            piece = str2[:2]
            if piece not in dic2:
                dic2[piece] = 1
            else:
                dic2[piece] += 1
        str2 = str2[1:]

    for i in dic1:
        if i not in dic_den:
            dic_den[i] = dic1[i]
        else:
            dic_den[i] += dic1[i]
        if i in dic2:
            dic_num[i] = dic1[i] if dic1[i] < dic2[i] else dic2[i]

    for j in dic2:
        if j not in dic_den:
            dic_den[j] = dic2[j]
        else:
            dic_den[j] = dic2[j] if dic1[j] < dic2[j] else dic_den[j]

    for x in dic_den:
        den += dic_den[x]
    for y in dic_num:
        num += dic_num[y]
        
    if den == 0:
        return 65536

    return math.floor(num / den * 65536)
