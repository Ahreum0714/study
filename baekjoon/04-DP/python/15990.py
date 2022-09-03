# https://www.acmicpc.net/problem/15990 1,2,3더하기 5 (python3:240ms / pypy3:160ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MOD = 1000000009

tc = int(input())

dp = [[0] * 3 for _ in range(100001)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] % MOD) + (dp[i-1][2] % MOD)
    dp[i][1] = (dp[i-2][0] % MOD) + (dp[i-2][2] % MOD)
    dp[i][2] = (dp[i-3][0] % MOD) + (dp[i-3][1] % MOD)

for _ in range(tc):
    n = int(input())
    print(sum(dp[n]) % MOD)