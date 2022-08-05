import sys
input = sys.stdin.readline

N = int(input())
tile = [0] * 1000001
mod = 15746

tile[1] = 1
tile[2] = 2

for k in range(3, N+1):
    tile[k] = (tile[k-1] + tile[k-2]) % mod

print(tile[N])