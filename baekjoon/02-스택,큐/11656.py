# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10430
import sys
sys.stdin = open('input.txt', 'r')

s = input()
suffix = []

for i in range(len(s)):
    suffix.append(s[i:])

print(*sorted(suffix), sep='\n')