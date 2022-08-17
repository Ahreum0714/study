# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10430
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)