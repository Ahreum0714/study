# [SWEA] D1 - 2063: 중간값 찾기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
scores = sorted(list(map(int, input().split())))
print(scores[N//2])