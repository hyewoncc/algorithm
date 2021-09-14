"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12915

전체 배열 길이가 최대 50이라 버블 정렬으로 해결 
람다식 공부가 필요하다...
"""

def solution(arr, n):
    x = len(arr)
    
    for i in range(x):
        for j in range(x-1):
            if arr[i][n] < arr[j][n]:
                arr[i], arr[j] = arr[j], arr[i]
            elif arr[i][n] == arr[j][n] and arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        
    return arr
