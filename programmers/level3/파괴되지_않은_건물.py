# 브루트 포스: O(N*M*K) -> 정확성은 맞으나 효율성 테스트 시간 초과
def cal(board, command):
    type, r1, c1, r2, c2, degree = command
    if type == 1:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] -= degree
    else:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += degree
    
def solution(board, skill):
    for s in skill:
        cal(board, s)
        
    cnt = 0
    for r in board:
        for c in r:
            if c >= 1: cnt += 1

    return cnt

# 누적합을 이용한 최적화 알고리즘
# https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-6-%ED%8C%8C%EA%B4%B4%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%80-%EA%B1%B4%EB%AC%BC
def acc(skill, br_len, bc_len):
    li = [[0] * (bc_len+1) for _ in range(br_len+1)]
    
    # 누적합을 위한 이차원 배열
    for type, r1, c1, r2, c2, degree in skill:
        li[r1][c1] += -degree if type == 1 else degree
        li[r1][c2+1] += degree if type == 1 else -degree
        li[r2+1][c1] += degree if type == 1 else -degree
        li[r2+1][c2+1] += -degree if type == 1 else degree

    # 행 기준 누적합
    for i in range(br_len):
        for j in range(bc_len):
            li[i][j+1] += li[i][j]
    
    # 열 기준 누적합
    for j in range(bc_len):
        for i in range(br_len):
            li[i+1][j] += li[i][j]
    
    return li
    
def solution(board, skill):
    cnt = 0
    acc_li = acc(skill, len(board), len(board[0]))
    
    for r in range(len(board)):
        for c in range(len(board[r])):
            board[r][c] += acc_li[r][c]
            if board[r][c] > 0: cnt += 1
    
    return cnt