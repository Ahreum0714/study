# https://www.acmicpc.net/problem/11726 2*n 타일링 2 (68ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dp = [0, 1, 3]
for i in range(3, 1001):
  dp.append((dp[i-1] + dp[i-2]*2) % 10007)
n = int(input())
print(dp[n])