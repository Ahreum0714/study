# [Prog] 완전탐색 - lv2: 카펫 https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for a in range(1, total + 1):
        if total % a == 0:
            b = total / a
            if a >= b and 2*a + 2*b - 4 == brown:
                answer = [a, b]
    return answer
'''
  그림을 그려보고 격자의 개수와 길이를 따져가며 공식을 구하면 된다.
  
전체 카펫의 가로가 a, 세로가 b일 때, 
노란색의 가로는 a-2, 세로는 b-2이다.
가로세로 길이와 격자의 개수의 관계성으로 3가지 조건식을 세울 수 있다.

1. a >= b
2. 2a + 2b - 4 = brown
3. (a-2)(b-2) = yellow
=> ab - 2a - 2b + 4 = yellow
=> ab = yellow + (2a + 2b - 4)
=> ab = yellow + brown

가로의 최대 길이 (yellow + brown) 까지 완전탐색하면서 위의 공식이 성립하는 a,b를 찾는다.
'''