# [SWEA] D2 - 1946: 간단한 압축 풀기
import sys, math
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    print(f'#{tc}')
    
    N = int(input())
    org = ''
    for i in range(N):
        doc = list(input().split())
        org += doc[0] * int(doc[1])
        while len(org) >= 10:
            print(org[:10])
            org = org[10:]
    print(org)