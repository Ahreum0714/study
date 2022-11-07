# [SWEA] D2 - 1959: 두 개의 숫자열
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if N > M:
        N, M = M, N
        a, b = b, a
    mx = 0
    for i in range(0, M-N+1):
        sum = 0
        for j in range(N):
            sum += a[j] * b[i+j]
        mx = max(sum, mx) if i > 0 else sum
        
    print(f'#{test_case} {mx}')