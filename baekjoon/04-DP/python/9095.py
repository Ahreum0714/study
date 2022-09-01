# https://www.acmicpc.net/problem/9095 1, 2, 3 더하기 (68ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for tc in range(int(input())):
    n = int(input())
    print(dp[n])