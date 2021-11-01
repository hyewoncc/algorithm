"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12953#

주어진 배열 수들의 최소공배수 구하기
배열이 짧아서 떠오르는대로 구현 
모든 수가 같은 엣지케이스에서 런타임 에러가 있어서 int 변환 추가해서 해결 
엣지케이스 테스트를 잘 하자! 
"""

def solution(arr):
    n = arr.pop()
    
    while len(arr) > 0:
        m = arr.pop()
        i = min(n, m)
        j = 1

        for x in range(2, i+1):
            if n%x == 0 and m%x == 0:
                j = x
        n = int(n * m / j)
        
    return n
  
