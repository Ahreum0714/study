# https://www.acmicpc.net/problem/10973 이전 순열 (48ms)
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

N = int(input())
seq = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if seq[i] < seq[i-1]:
        x, y = i-1, i
        for j in range(N-1, 0, -1):
            if seq[j] < seq[x]:
                seq[j], seq[x] = seq[x], seq[j]
                seq = seq[:i] + sorted(seq[i:], reverse=True)
                print(*seq)
                exit(0)
print(-1)