# [SWEA] D1 - 2063: 중간값 찾기
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
print(*list(range(N, -1, -1)))