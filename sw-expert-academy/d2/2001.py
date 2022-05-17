import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] for _ in range(N)]
    for i in range(N):
        matrix[i] = list(map(int, input().split()))

    max = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            sum = 0
            for rt in range(M):  #row of temp (temp: M*M)
                for ct in range(M):
                    sum += matrix[r+rt][c+ct]
            if max < sum:   max = sum
            
    print(f'#{test_case} {max}')