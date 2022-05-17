import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0] * len(won)

    for i in won:
        quotient = N // i
        if quotient > 0:
            idx = won.index(i)
            cnt[idx] = quotient
            N = N % i
            if N == 0: break
    
    print(f'#{test_case}')
    print(*cnt)