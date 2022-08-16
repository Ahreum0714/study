# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/11655 
import sys
sys.stdin = open('input.txt', 'r')

s = sys.stdin.readline()
ans = ''
alpha_num = ord('z') - ord('a') + 1

# 방법 1  (72ms)
for c in s:
    if c.islower():
        asc = ord(c) + 13
        if asc > ord('z'):
            asc -= alpha_num
        ans += chr(asc)
    elif c.isupper():
        asc = ord(c) + 13
        if asc > ord('Z'):
            asc -= alpha_num
        ans += chr(asc)
    else:
        ans += c
print(ans)


# 방법 2  (68ms)
for c in s:
    if c.islower():
        asc = ord(c) + 13
        if asc > ord('z'):
            asc = ord('a') + (asc - ord('a')) % alpha_num
        ans += chr(asc)
    elif c.isupper():
        asc = ord(c) + 13
        if asc > ord('Z'):
            asc = ord('A') + (asc - ord('A')) % alpha_num
        ans += chr(asc)
    else:
        ans += c
print(ans)

            # a b c d e f  |6개
            # 0 1 2 3 4 5  |idx

            # 1+4 = 5
            # 2+4 = 6
            # 6 - 6 = 0
            # 3+4 = 7
            # 7 - 6 = 1