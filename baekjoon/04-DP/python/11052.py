# https://www.acmicpc.net/problem/11052 카드 구매하기 (68ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], p[k] + dp[i-k])

print(dp[n])