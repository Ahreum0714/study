# https://www.acmicpc.net/problem/2193 이친수 (76ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
dp = [1] * 91
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] # 끝자리 0,1 구분해서 하나씩 구하는 것보다 해당 점화식이 더 간단해서 이 방법으로 구현함

print(dp[n])