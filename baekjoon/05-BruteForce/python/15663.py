# https://www.acmicpc.net/problem/15663 N과 M(9) (128ms)
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

tmp = []
visited = [False] * n

def dfs():
    if len(tmp) == m:
        print(*tmp)
        return

    memo = 0
    for i in range(n):
        if not visited[i] and memo != numbers[i]:
            visited[i] = True
            tmp.append(numbers[i])
            memo = numbers[i]
            dfs()
            visited[i] = False
            tmp.pop()
        
dfs()