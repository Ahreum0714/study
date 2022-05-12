T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    sum_num = sum(nums)
    avg = sum_num/10  #round(sum_num/10) 하니까 런타임 에러 났음... 분리시켜주니까 실행시간 단축되고 통과!
    print(f'#{test_case} {round(avg)}')