"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

딕셔너리를 사용 
문자열을 모아서 딕셔너리와 일치하면 교체해주는 방식으로 했으나 
문자열의 replace 기능을 사용하면 훨씬 쉽게 할 수 있었다 
파이썬 문자열 공부할 것 
"""

def solution(s):
    num_str = ""
    answer = ""
    nums = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for x in s:
        if x in "0123456789":
            answer += x
        else:
            num_str += x
            
            if num_str in nums.keys():
                answer += nums[num_str]
                num_str = ""
                
    return int(answer)
