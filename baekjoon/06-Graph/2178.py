# https://www.acmicpc.net/problem/2178 미로 탐색 (BFS: 112ms)
# 최단 거리는 BFS 방식!
# 도착지 노드에 도착하는 순간이 바로 최단 경로이기 때문에 DFS와 달리 방문했던 노드를 재방문할 필요가 없음
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque([(x, y)])
    while q:
        a, b = q.popleft()
        for i in range(len(dx)):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue
            
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[a][b] + 1
                q.append((nx, ny))

    return miro[n-1][m-1]

print(bfs(0, 0))