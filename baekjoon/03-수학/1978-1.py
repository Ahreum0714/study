# https://www.acmicpc.net/problem/1978 소수 찾기 (40ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

MAX = 1000
prime_num = [False] + [True for _ in range(MAX)]
prime_num[1] = False

for i in range(2, MAX+1):
    if prime_num[i]:
        for j in range(2, MAX//i+1):
            prime_num[i*j] = False

n = int(input())
nums = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if prime_num[nums[i]]:
        cnt += 1

print(cnt)