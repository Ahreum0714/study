import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
arr = list(map(int, input().split()))
dp = [-1000 for _ in range(n)]

dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))