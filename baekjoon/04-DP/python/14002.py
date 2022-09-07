# https://www.acmicpc.net/problem/14002 가장 긴 증가하는 부분 수열 4 (ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) # 10 20 10 30 20 50 => 10 20 30 50
dp = [1 for _ in range(n)]

# 길이 구하기
for i in range(n):
    for j in range(i):
        if a[i] > a[j]: 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 부분 수열 구하기 
# (가장 긴 부분 수열의 조건에 맞을 때마다 원소가 추가되면서 길이가 +1 됨)
# (= dp에 해당하는 원소값은 현재 인덱스값이 앞 원소들보다 몇번째로 큰지에 대한 순서와 같음)
# (=> dp 인덱스와 리스트 a의 인덱스를 매칭시켜서 부분 수열을 구할 수 있음)
order = max(dp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == order:
        result.append(a[i])
        order -= 1

print(*result[::-1])