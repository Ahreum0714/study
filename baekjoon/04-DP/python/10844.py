# https://www.acmicpc.net/problem/10844 쉬운 계단 수 (ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MOD = 1000000000

n = int(input())
dp = [[0] * 10 for _ in range(101)]
dp[1] = [0] + [1 for _ in range(9)]

for i in range(2, n+1):
    for k in range(10):
        if k == 0:
            dp[i][0] = dp[i-1][1]
        elif k == 9:
            dp[i][9] = dp[i-1][8]
        else:
            dp[i][k] = dp[i-1][k-1] + dp[i-1][k+1]

print(sum(dp[n]) % MOD)