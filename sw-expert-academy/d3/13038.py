from operator import index
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input()) # 수업을 들으려는 n일
    week = list(map(int, input().split())) # 시간표
    ans = 1e9
    
    for i in range(7):
        if week[i] == 1:
            idx = i
            tmp_n = n
            tmp_ans = 0
            while tmp_n:
                if week[idx] == 1:
                    tmp_n -= 1
                tmp_ans += 1
                idx = (idx + 1) % 7
            
            if tmp_ans < ans:
                ans = tmp_ans
    
    print(f'#{test_case} {ans}')