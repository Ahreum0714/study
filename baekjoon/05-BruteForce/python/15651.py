# https://www.acmicpc.net/problem/15651 N과 M (3) (1856ms)
from itertools import product
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
for i in product(range(1, n+1), repeat=m):
    print(*i)