# [Prog] DFS/BFS - lv2: 게임 맵 최단거리
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    q = deque([(0,0)])
    bfs(q, maps)
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1

def bfs(q, maps):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[a][b] + 1
                q.append((nx, ny))