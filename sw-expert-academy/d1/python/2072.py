T = int(input())
for test_case in range(1, T+1):
    sum = 0
    num = list(map(int, input().split(" ")))
    for j in num:
        if (j % 2 == 1):
            sum += j
    print(f'#{test_case} {sum}')