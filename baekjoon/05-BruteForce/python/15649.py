# https://www.acmicpc.net/problem/15649 N과 M (1) (180ms)
from itertools import permutations
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
n, m = map(int, input().split())
ans = permutations(range(1,n+1), m)
for i in list(ans):
    print(*i)