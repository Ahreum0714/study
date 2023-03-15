# https://www.acmicpc.net/problem/10818 최소, 최대 (400ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
li = sorted(list(map(int, input().split())))

print(min(li), max(li))