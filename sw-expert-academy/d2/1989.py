import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    origin = input().strip()
    tmp = list(origin)
    tmp.reverse()
    rev = ''.join(tmp)
    
    print(f'#{test_case} {1 if origin == rev else 0}')
    