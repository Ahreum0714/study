# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1676
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

n = int(input())
fac = str(factorial(n))
cnt = 0
for i in fac[::-1]:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break
