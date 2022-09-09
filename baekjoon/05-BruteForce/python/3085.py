# https://www.acmicpc.net/problem/3085 사탕 게임 (python3: 4608ms / pypy3: 500ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
N의 크기가 50이므로 브루트포스 탐색이 가능하다
  1.가로로 양옆의 사탕을 바꾸고 연속된 최대 개수를 카운트한다
  2.세로로 상하의 사탕을 바꾸고 연속된 최대 개수를 카운트한다
'''
n = int(input())
candy = [list(input().rstrip()) for _ in range(n)]
ans = 1

# 몇 개 먹을 수 있는지 찾는 함수
def count_candy():
    global ans    
    # 행에서의 최대 개수 카운트
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[i][j] == candy[i][j+1]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
    # 열에서의 최대 개수 카운트
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

# [모든 인접한 두 자리 뒤집어보고 최대 개수 찾기]
# 가로 뒤집기
for i in range(n):
    for j in range(n-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # 양옆 위치를 바꾸고
        count_candy()
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] # 위치 원상 복귀
# 세로 뒤집기
for i in range(n):
    for j in range(n-1):
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        count_candy()
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(ans)