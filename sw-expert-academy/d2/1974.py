import sys
sys.stdin = open("input.txt", "r")

def row_valid(sudoku):
    for r in range(9):
        visit = [False] * 10  # 1~9 숫자별 방문여부 확인. 0번째 인덱스는 버리는 값
        for c in range(9):
            val = sudoku[r][c]
            
            if visit[val] == True:
                return 0
            else:
                visit[val] = True
    return 1

def col_valid(sudoku):
    for c in range(9):
        visit = [False] * 10  # 1~9 숫자별 방문여부 확인. 0번째 인덱스는 버리는 값
        for r in range(9):
            val = sudoku[r][c]

            if visit[val] == True:
                return 0
            else:
                visit[val] = True
    return 1

def square_valid(sudoku):
    for r_start in range(0, 9, 3):
        for c_start in range(0, 9, 3):
            visit = [False] * 10  # 1~9 숫자별 방문여부 확인. 0번째 인덱스는 버리는 값
            for i in range(3):
                for j in range(3):
                    val = sudoku[r_start + i][c_start + j]

                    if visit[val] == True:
                        return 0
                    else:
                        visit[val] = True
    return 1
            
T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]    # 9*9 크기의 스도쿠
    
    r = row_valid(sudoku)
    c = col_valid(sudoku)
    s = square_valid(sudoku)   

    if (r == 0 or c == 0 or s == 0):
        ans = 0
    else:
        ans = 1
    
    print(f'#{test_case} {ans}')