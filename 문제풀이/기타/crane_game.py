"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/64061

지문대로 차근차근 구현  
다른 기출문제 풀 때 코드부터 짜지 않고 단계를 확실히 한 다음 하기로 했는데, 
난이도 차이가 있었겠지만 그렇게 하니 확실히 시간이 단축되었다  
"""
def solution(board, moves):
    dolls = []
    size = len(board)
    answer = 0
    
    for m in moves:
        i = 0
        while i < size:
            if board[i][m-1] != 0:
                dolls.append(board[i][m-1])
                board[i][m-1] = 0
                break
            i += 1
                
        if len(dolls) > 1:
            if dolls[-2] == dolls[-1]:
                answer += 2
                dolls = dolls[:-2]
    
    return answer
