T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    max_cnt = 0
    ans = 0

    for i in range(100, -1, -1):
        c = li.count(i)
        if max_cnt < c:
            max_cnt = c
            ans = i
            
    print(f'#{n} {ans}')