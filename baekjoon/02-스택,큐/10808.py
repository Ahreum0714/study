# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10808
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

S = list(input().strip())
alphabet = [chr(ord('a')+i) for i in range(ord('z')-ord('a')+1)]
cnt = [0] * (ord('z') - ord('a') + 1)
for c in S:
    if c in alphabet:
        cnt[alphabet.index(c)] += 1

print(*cnt)