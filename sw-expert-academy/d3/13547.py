import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    S = input()
    cnt = 0
    for _ in S:
        if _ == 'x':    cnt += 1

    if cnt <= 15 - 8: print(f'#{test_case} YES')
    else: print(f'#{test_case} NO')