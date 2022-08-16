# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10824
import sys
sys.stdin = open('input.txt', 'r')

a, b, c, d = sys.stdin.readline().split()
print(int(a+b) + int(c+d))

# (68ms)