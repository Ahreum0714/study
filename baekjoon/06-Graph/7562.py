# https://www.acmicpc.net/problem/7562 나이트의 이동 (BFS: 2468ms)
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

tc = int(input())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        if a == to[0] and b == to[1]:
            return board[a][b]
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[a][b] + 1
                q.append((nx, ny))             

for _ in range(tc):
    l = int(input())
    board = [[0]* l for _ in range(l)]
    now = tuple(map(int, input().split()))
    to = tuple(map(int, input().split()))
    
    if now == to:
        print(0)
    else:
        print(bfs(now[0], now[1]))