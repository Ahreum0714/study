# https://www.acmicpc.net/problem/11724 연결 요소의 개수 (872ms)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(((10**5)))   # 해당 리밋 없으면 dfs시 런타임 에러 발생
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def dfs(start):
    if visited[start] == False:
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                dfs(i)
        return True

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        ans += 1
        # if dfs(i):
        #     ans += 1

print(ans)