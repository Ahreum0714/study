# https://www.acmicpc.net/problem/7576 토마토 (BFS: 2264ms)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans =0

def init():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                q.append((i, j))

def bfs():
    while q:
        a, b = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[a][b] + 1
                q.append((nx, ny))

def verify():
    global ans
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                print(-1)
                exit()
            ans = max(box[i][j], ans)
    ans -= 1

init()
bfs()
verify()
print(ans)