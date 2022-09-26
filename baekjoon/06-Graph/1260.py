# https://www.acmicpc.net/problem/1260 DFS와 BFS (104ms)
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m, start = map(int, input().split())
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort() # 작은 노드부터 방문해야 하므로

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            # visited[i] = True

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(start)
visited = [False] * (n+1)
print()
bfs(start)