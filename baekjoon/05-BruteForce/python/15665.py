# https://www.acmicpc.net/problem/15665 N과 M(11) (748ms)
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))

tmp = []

def dfs():
    if len(tmp) == m:
        print(*tmp)
        return

    for num in numbers:
        tmp.append(num)
        dfs()
        tmp.pop()
        
dfs()