# https://www.acmicpc.net/problem/2225 합분해 (84ms)
import sys
# import time
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# start = time.time()
N, K = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]
for i in range(201):
    dp[1][i] = 1     # dp[k][n] : k=1 일 때 항상 1개의 경우의 수를 가짐
    dp[2][i] = i + 1 # dp[k][n] : k=2 일 때 항상 N+1개의 경우의 수를 가짐
    dp[i][1] = i     # dp[k][n] : n=1 일 때 항상 k개의 경우의 수를 가짐

for i in range(3, 201):
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1e9

print(int(dp[K][N]))
# end = time.time()
# print(f'{end-start: .5f} sec')