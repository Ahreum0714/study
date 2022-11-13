# [SWEA] D3 - 1206: [S/W 문제해결 기본] 1일차 - View
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

for t in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    view = 0
    for i in range(2, N - 2):
        l2 = building[i] - building[i-2]
        l1 = building[i] - building[i-1]
        r1 = building[i] - building[i+1]
        r2 = building[i] - building[i+2]
        if l2 > 0 and l1 > 0 and r1 > 0 and r2 > 0 :
            view += min(l2, l1, r1, r2)
    
    print(f'#{t} {view}')
        