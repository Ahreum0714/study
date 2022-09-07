# https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열 (ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]: 
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))