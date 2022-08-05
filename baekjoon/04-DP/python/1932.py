import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
tri = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

# dp 초기화 (입력받은 tri값은 그대로 넣어주고 나머지 인덱스는 0으로 채우기)
for r in range(len(tri)):
    for c in range(len(tri[r])):
        dp[r][c] = tri[r][c]
# print(dp)

# 합의 최대값을 구하기 위한 dp 수행
for h in range(1, N):
    for i in range(h+1):
        if i == 0:
            dp[h][i] += dp[h-1][i]
        else:
            dp[h][i] += max(dp[h-1][i-1], dp[h-1][i])
# print(dp)

# dp 마지막 행 중 max값이 합의 최대
print(max(dp[-1]))
