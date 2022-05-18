import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    li = list(map(int, input().split()))
    li.sort()
    end = len(li)
    li = li[1:end-1]
    avg = sum(li) / len(li)
    print(f'#{test_case} {round(avg)}')