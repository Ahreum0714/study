# https://www.acmicpc.net/problem/13023 ABCDE (DFS: 1188ms)
import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(idx, count):
    if count == 4:
        print(1)
        exit()
    next = friends[idx]
    for i in next:
        if not visited[i]:
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)