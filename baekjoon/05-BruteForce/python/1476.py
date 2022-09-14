# https://www.acmicpc.net/problem/1476 날짜계산 (72ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
E, S, M = map(int, input().split())
e, s, m, year = 1, 1, 1, 1
while(True):
    if E == e and S == s and M == m:
        print(year)
        exit()
    e += 1; s += 1; m += 1; year += 1
    if e > 15:  e = 1
    if s > 28:  s = 1
    if m > 19:  m = 1