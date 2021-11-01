"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/67256

주어진 지문대로 단계별 생각 후 구현
어려워보여서 미루던 문제인데 해보니 쉬웠다...
구상한 단계를 그대로 옮기다 보니 다른 사람들 코드 보다 난잡한 감이 있다  
"""

def solution(numbers, hand):
    keypad = {1: [0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], '*':[3,0], 0:[3,1], '#':[3,2]}
    left = ['*']
    right = ['#']
    answer = []
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer.append('L')
            left.append(n)
        elif n in[3, 6, 9]:
            answer.append('R')
            right.append(n)
        else:
            l_index = keypad[left[-1]]
            r_index = keypad[right[-1]]
            l_distance = abs(keypad[n][0] - l_index[0]) + abs(keypad[n][1] - l_index[1])
            r_distance = abs(keypad[n][0] - r_index[0]) + abs(keypad[n][1] - r_index[1])
            if l_distance < r_distance:
                answer.append('L')
                left.pop()
                left.append(n)
            elif l_distance > r_distance:
                answer.append('R')
                right.pop()
                right.append(n)
            else:
                if hand == "left":
                    answer.append('L')
                    left.append(n)
                else:
                    answer.append('R')
                    right.append(n)

    return "".join(answer)
  
  
