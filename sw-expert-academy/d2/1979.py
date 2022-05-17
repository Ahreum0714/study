import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [[0] * (N) for _ in range(N)]
    for i in range(N):
        matrix[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        cnt = [0,0]  # 0:가로 1:세로
        for j in range(N):
            #가로
            if matrix[i][j] == 0:
                if cnt[0] == K: 
                    ans += 1
                cnt[0] = 0
            else:   
                cnt[0] += 1
            # 세로
            if matrix[j][i] == 0:
                if cnt[1] == K: 
                    ans += 1
                cnt[1] = 0
            else:
                cnt[1] += 1
        if cnt[0] == K: ans += 1
        if cnt[1] == K: ans += 1
    
    print(f'#{test_case} {ans}')
    