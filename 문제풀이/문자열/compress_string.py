"""
프로그래머스
https://programmers.co.kr/learn/courses/30/lessons/60057

문자열을 조건에 맞게 압축하고, 최적해 찾기
풀이 구상은 괜찮았으나, 엣지케이스 검사가 부족했다
여러 경우의 수를 꼼꼼히 생각해보기
"""

def solution(s):
    n = len(s)
    answer = []
    get_piece = True
    
    if n == 1:
        return 1
    
    for i in range(1, n//2+1):
        m = n
        count = 0
        head = 0
        nums = 0
        for j in range(0, n, i):
            if get_piece:
                piece = s[j:j+i]
            if s[j+i:].startswith(piece):
                m -= i
                count += 1
                get_piece = False
            else:
                if not get_piece:
                    head = len(str(count+1))
                    nums += head
                    count = 0
                get_piece = True
        answer.append(m+nums)
    return min(answer)
