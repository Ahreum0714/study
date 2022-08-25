# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/17087 숨바꼭질6 (132ms)
import math
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. a 원소 각각마다 (s - a 원소)의 차를 모두 구한다
# 2. 차들의 최대 공약수를 구한다
n, s = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

if n == 1:
    ans = abs(a[0] - s)
else:
    difference = [abs(s - a[i]) for i in range(len(a))]
    ans = difference[0]
    for i in range(1, len(difference)):
        ans = math.gcd(ans, difference[i])

print(ans)