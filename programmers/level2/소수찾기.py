# [Prog] 완전탐색 - lv2: 소수 찾기  https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    li = []
    for i in range(1, len(numbers)+1):
        for el in permutations(numbers, i):
            tmp = ''
            for digit in el:
                tmp += digit
            li.append(int(tmp))
            
    for num in set(li):
        if isPrime(num):
            answer += 1
         
    return answer