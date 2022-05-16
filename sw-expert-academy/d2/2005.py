# 방법 1
def solve(N):
    pascal = []
    for h in range(0, N):
        if h == 0: 
            pascal.append([1])
        elif h == 1: 
            pascal.append([1,1])
        else:
            tmp = [1]
            for i in range(0, h-1): # 구현 코드에서는 h가 1이 아니라 0부터 시작하기 때문에 h-2가 아니라 h-1
                tmp.append(pascal[h-1][i] + pascal[h-1][i+1])
            tmp.append(1)
            pascal.append(tmp)
    return pascal

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = solve(N)
    print(f'#{test_case}')
    for h in range(0, N):
        print(*result[h])


# 방법 2
def solve(N):
    pascal = [[0] * N for _ in range(N)]
    pascal[0][0] = 1 # 첫번째 줄 초기화
    for h in range(1, N): # 두번째 줄 부터 규칙 적용
        for col in range(N):
            if col == 0:
                pascal[h][col] = 1
            else:
                pascal[h][col] = pascal[h-1][col-1] + pascal[h-1][col]
    return pascal

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = solve(N)
    print(f'#{test_case}')
    for h in range(0, N):
        li = [el for el in result[h] if el > 0]
        print(*li)