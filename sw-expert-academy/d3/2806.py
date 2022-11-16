# [SWEA] D3 - 2806: N-Queen
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def diagonal(cur_r, cur_c):
    for i in range(cur_r):
        if (cur_r - i) == abs(cur_c - r_visit[i]):
            return True
    return False

def dfs(r_idx):
    global cnt
    if r_idx == N:
        cnt += 1
        return
    
    for c_idx in range(N):
        if c_visit[c_idx]: continue
        if diagonal(r_idx, c_idx): continue
        c_visit[c_idx] = 1
        r_visit[r_idx] = c_idx
        dfs(r_idx + 1)
        c_visit[c_idx] = 0
        
for tc in range(1, T + 1):
    N = int(input())
    r_visit = [0 for _ in range(N)] # r_visit[행idx] = idx번째 행의 열 인덱스 값
    c_visit = [0 for _ in range(N)] # c_visit[열idx] = 0/1 : idx번재 열 방문 여부 기록
    cnt = 0
    
    dfs(0)
    print(f'#{tc} {cnt}')