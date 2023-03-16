# https://www.acmicpc.net/problem/10972 피보나치 수5 (40ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
fibo = [0, 1]

if n < 2:
    print(fibo[n])
else:
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    print(fibo[n])