# [SWEA] D3 - 1206: [S/W 문제해결 기본] 1일차 - Flatten
import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for i in range(dump):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1
    boxes.sort()
    print(f'#{test_case} {boxes[-1] - boxes[0]}')