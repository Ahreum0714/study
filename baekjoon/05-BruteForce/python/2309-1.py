# https://www.acmicpc.net/problem/10972 일곱 난쟁이 (ms)
'''
    230316 재풀이
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

candidate = sorted([int(input()) for _ in range(9)])
ans = []

for i in range(len(candidate)-1):
    for j in range(i+1, len(candidate)):
        if sum(candidate) - candidate[i] - candidate[j] == 100:
            ans = [val for val in candidate if val != candidate[i] and val != candidate[j]]
            print(*ans, sep='\n')
            exit()  # 이중 for문 바로 빠져나갈 수 있게 한번에 exit 시킴