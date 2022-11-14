# [Prog] 완전탐색 - lv2: 모음사전 https://school.programmers.co.kr/learn/courses/30/lessons/84512

# 리스트 컴프리헨션으로 다듬은 코드
from itertools import product

def solution(word):
    dict = [''.join(list(j)) for i in range(1, 6) for j in product('AEIOU', repeat=i)]
    dict.sort()
    return dict.index(word) + 1

# 처음 작성 코드
from itertools import product, chain

def solution(word):
    alpha = ['A','E','I','O','U']
    dict = []
    for i in range(1, 6):
        dict.append(list(product(alpha, repeat=i)))

    dict = sorted(list(chain(*dict)))
    for idx, val in enumerate(dict):
        tmp = ''
        for el in val:
            tmp += el
        dict[idx] = tmp

    return dict.index(word) + 1