# https://www.acmicpc.net/problem/14500 테트로미노 (2번 풀이법으로 252ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

###################### 1. ㅗ 블럭을 따로 처리해주는 방법 ########################
# 참고 블로그: https://cijbest.tistory.com/87 (python3 시간초과 / pypy3 872ms)

# INPUT
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 우, 좌, 하, 상
move = [(0,1), (0,-1), (1,0), (-1,0)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum+paper[ni][nj], cnt+1)
            visited[ni][nj] = False

# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = paper[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k) % 4
            ni = i + move[t][0]
            nj = j + move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += paper[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)

for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)


############# 2. dfs 수행중에 2까지일 대 시작점을 자기자신으로 하는 dfs를 호출함으로써 ㅗ 처리를 밖으로 빼지 않는 방법 #############
# 참고 블로그: https://esoongan.tistory.com/187 (python3: 252ms) & https://heytech.tistory.com/364 (설명은 여기가 더 자세함)
move = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(r, c, depth, s):
    global max_value
    # 종료조건1) 탐색을 계속 진행하여도 최댓값에 못 미치는 경우
    if s + maxv*(4-depth) <= max_value:
        return        

    # 종료조건2) 블록 4개를 모두 활용한 경우
    if depth >= 4:
        if max_value < s:
            max_value = s
        return
        
    # 상하좌우 방향으로 블록 이어 붙여 나가기
    else:
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            # 새로운 좌표가 유효한 범위 내 있고 탐색이력이 없는 경우
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                # 2번째 블록 연결 후 'ㅏ','ㅓ','ㅗ','ㅜ' 만들기
                if depth == 2:
                    visited[nr][nc] = 1
                    # 새로운 좌표에서 탐색하지 않고 기존 좌표로 돌아와 탐색재개
                    dfs(r, c, depth + 1, s + board[nr][nc])
                    visited[nr][nc] = 0

                visited[nr][nc] = 1
                dfs(nr, nc, depth + 1, s + board[nr][nc])
                visited[nr][nc] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxv = max(map(max, board))

max_value = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0

print(max_value)

'''
핵심 아이디어는 DFS를 통해 모양들을 만드는 것이다.
테트로미노는 모두 정사각형 4개를 이어붙여 만든 도형들이므로 4번 움직인 경로는 모두 테트로미노 모양이 될 것이다.
그러나, 이러한 경로로 담아낼 수 없는 모양이 있다. 바로 'ㅏ' 모양이다.
이 모양을 만들기 위해 한 번 다음 목적지의 visited는 체크하되, 움직이지 않는 것이 필요하다.
그리고 여기까지 떠올렸다고 해도 훌륭한 것이라고 생각하지만, 우리가 사용하는 언어는 파이썬이기에 시간복잡도를 줄이기 위해 한 가지 트릭을 더 사용해야 한다.
DFS로 모든 경우의 수를 시험해볼 수 있지만, 사실 겹치거나 필요없는 경우를 시도하게 될 때가 있다.
이러한 시도를 최소화하기 위해 전체 수들 중에서 최댓값 max_val을 구한 후, 
DFS 중에 남은 경로의 자취가 모두 최댓값이 나온다고 하더라도 현재의 답을 갱신할 수 없을 때, 
그 search는 끝내도록 하는 것이다.
'''