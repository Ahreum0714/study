# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10820
import sys
sys.stdin = open('input.txt', 'r')

## 1번째 나의 풀이 (76ms)
# lower = [chr(ord('a')+i) for i in range(ord('z')-ord('a')+1)]
# upper = [chr(ord('A')+i) for i in range(ord('Z')-ord('A')+1)]
# digit = [str(i) for i in range(10)]
# space = ' '

# while True:
#     line = sys.stdin.readline().rstrip('\n')
    
#     if not line: # 아무것도 입력되지 않았을 때 예외처리
#         break
    
#     l, u, d, s = 0, 0, 0, 0
#     for c in line:
#         if c in lower:
#             l += 1
#         elif c in upper:
#             u += 1
#         elif c in digit:
#             d += 1
#         elif c in space:
#             s += 1
    # print(l, u, d, s)


# 2번째 다른 사람 풀이 참고 (72ms)
while True:
    line = sys.stdin.readline().rstrip('\n')
    
    if not line: # 아무것도 입력되지 않았을 때 예외처리
        break
    
    l, u, d, s = 0, 0, 0, 0
    for c in line:
        if c.islower():
            l += 1
        elif c.isupper():
            u += 1
        elif c.isdigit():
            d += 1
        elif c.isspace():
            s += 1
    print(l, u, d, s)