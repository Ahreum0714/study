# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/2743
import sys
sys.stdin = open('input.txt', 'r')
S = sys.stdin.readline()
ans = 0
for i in S:
    if i.isalpha():
        ans += 1
print(ans)

## 이렇게만 해도 되네... 
#print(len(input()))