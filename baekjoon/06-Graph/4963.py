# https://www.acmicpc.net/problem/4963 섬의 개수 (BFS: 112ms, DFS:104ms)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline()

def dfs(x, y):
    # 상, 하, 좌, 우, 대각선
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    m[x][y] = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:
            dfs(nx, ny) 

def bfs(x, y):
    # 상, 하, 좌, 우, 대각선
    dx = [0, 0, -1, 1, -1, 1, 1, -1]
    dy = [-1, 1, 0, 0, -1, -1, 1, 1]
    m[x][y] = 0
    q = deque([[x, y]])
    while q:
        a, b = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i] 
            ny = b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and m[nx][ny] == 1:
                m[nx][ny] = 0
                q.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()

    cnt = 0
    m = [[] * w for _ in range(h)]
    for i in range(h):
        m[i] = list(map(int, input().split()))

    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                # bfs(i, j)
                dfs(i, j)
                cnt += 1
    print(cnt)