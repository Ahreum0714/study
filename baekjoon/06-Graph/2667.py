# https://www.acmicpc.net/problem/2667 단지번호붙이기 (BFS: 92ms, DFS:88ms)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline()

n = int(input())
house = []
per = []
for i in range(n):
    house.append(list(map(int, input().rstrip())))

def dfs(x, y):
    dx = [0, 0, -1, 1] # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    global cnt

    if house[x][y] == 1:
        house[x][y] = 0
        cnt += 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == 1:
            dfs(nx, ny)

def bfs(x, y):
    dx = [0, 0, -1, 1] # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    q = deque([[x, y]])
    house[x][y] = 0
    cnt = 1

    while q:
        a, b = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == 1:
                cnt += 1
                house[nx][ny] = 0
                q.append([nx, ny])
    return cnt

for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            # # --- BFS ---
            # per.append(bfs(i, j))
            
            # --- DFS ---
            cnt = 0
            dfs(i, j)
            per.append(cnt)

print(len(per))
for v in sorted(per):
    print(v)