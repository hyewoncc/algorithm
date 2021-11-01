"""
프로그래머스 
https://programmers.co.kr/learn/courses/30/lessons/12977

주어진 수에서 세 수를 더했을 때 소수인지 검사 후 개수 반환하기 
시간초과 걸리진 않았으나 다른 언어에서는 같은 로직으로 걸리는 경우 있음 
따라서, 매번 isPrime으로 소수 검증을 하지 않고, 
세 수의 최대수인 3000까지의 소수를 에라토스테네스의 체로 구해서 배열을 만들어 놓고, 
그 배열에서 확인하면 숫자를 줄일 수 있음 
"""
def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    l = len(nums)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                m = nums[i] + nums[j] + nums[k]
                if isPrime(m):
                    answer += 1

    return answer
  
  
