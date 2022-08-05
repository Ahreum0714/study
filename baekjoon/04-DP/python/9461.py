import sys
input = sys.stdin.readline

P = [0 for _ in range(101)]
P[1], P[2], P[3], P[4], P[5] = 1, 1, 1, 2, 2

for i in range(6, 101):
        P[i] = P[i-1] + P[i-5]

T = int(input())
for t in range(T):
    print(P[int(input())])