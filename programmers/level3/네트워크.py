# [Prog] DFS/BFS - lv3: 네트워크
from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, n, computers, visited)
            dfs(i, n, computers, visited)
            answer += 1
    return answer

def dfs(start, n, computers, visited):
    visited[start] = True
    for i in range(n):
        if computers[start][i] == 1 and not visited[i]:
            dfs(i, n, computers, visited)

def bfs(start, n, computers, visited):
    visited[start] = True
    q = deque([start])
    while q:
        next = q.popleft()
        for i in range(n):
            if computers[next][i] == 1 and not visited[i]:
                visited[i] = True
                q.append(i)