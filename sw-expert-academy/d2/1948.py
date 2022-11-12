# [SWEA] D2 - 1948: 날짜 계산기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    first, second = li[:2], li[2:]
    ans = 0
    if first[0] == second[0]:
        ans = second[1] - first[1] + 1
    else:
        ans = day[first[0]] - first[1] + 1 + second[1]
        for month in range(first[0] + 1, second[0]):
            ans += day[month]
            
    print(f'#{tc} {ans}')