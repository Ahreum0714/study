# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1978
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = input()
num = map(int, input().strip().split())
cnt = 0

for i in num:
    if i > 1:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            cnt += 1
print(cnt)
# (68ms)