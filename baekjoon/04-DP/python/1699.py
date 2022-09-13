# https://www.acmicpc.net/problem/1699 제곱수의 합 (python3: 6204ms / pypy3: 176ms)
import math
import sys
sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline())
'''
n  | term
1  | 1
2  | 1+1
3  | 1+1+1
4  | 2^2 = dp[4]
5  | 2^2 + 1
6  | 2^2 + 1 + 1
7  | 2^2 + 1 + 1 + 1
8  | 2^2 + 2^2
9  | 3^2 = dp[9]
'''
dp = [x for x in range(n+1)]
for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i - j*j] + 1

print(dp[n])

############## python3 4140ms 풀이 ##############
import sys

N = int(sys.stdin.readline().strip())
dp = [i for i in range(N + 1)]
square_number = [i ** 2 for i in range(1, int(N ** 0.5) + 1)] # sqrt 말고 **0.5 도 가능하다! 심지어 속도도 더 빠르다...!

for i in range(1, N + 1) :
    for j in square_number :
        if j > i:
            break
        if dp[i] > dp[i - j] + 1 :
            dp[i] = dp[i - j] + 1

print(dp[N])