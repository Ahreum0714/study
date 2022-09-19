# https://www.acmicpc.net/problem/15650 N과 M (2) (68ms)
from itertools import combinations
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
ans = combinations(range(1, n+1), m)
for i in ans:
    print(*i)