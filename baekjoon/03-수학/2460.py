# https://www.acmicpc.net/problem/2460 지능형 기차2 (40ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

passenger = 0
max_passenger = 0

for i in range(10):
    out_, in_ = map(int, input().split())
    passenger += in_ - out_
    max_passenger = max(passenger, max_passenger)

print(max_passenger)