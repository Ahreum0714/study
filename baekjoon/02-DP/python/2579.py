import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
stair = [0] * (N+1)
for i in range(1, N+1):
    stair[i] = int(input())

# N의 개수가 1 혹은 2인 경우를 고려하여 출력 후 종료시켜야 함
if N == 1:
    print(stair[1])
    exit()
if N == 2:
    print(stair[1] + stair[2])
    exit()

# 초기화
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
# 최대값을 구하기 위한 dp 수행
for i in range(3, N+1):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(dp[-1])

