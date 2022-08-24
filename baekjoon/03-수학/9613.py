# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/9613 GCD합 (72ms)
import math
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

for tc in range(int(input())):
    li = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(li)):
        for j in range(i+1, len(li)):
            ans += math.gcd(li[i], li[j])
    print(ans)