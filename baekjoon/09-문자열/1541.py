# https://www.acmicpc.net/problem/1541 잃어버린 괄호 (ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

expr = input().split('-')
sum = 0
for i in expr[0].split('+'):
    sum += int(i)
for i in expr[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)