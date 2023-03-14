# https://www.acmicpc.net/problem/3460 이진수 (52ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end=' ')