import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

stack = []
T = int(input())

# 방법 1 - 스택 & extend
for _ in range(T):
    words = input().split()
    for i in words:
        stack.extend(i) # append를 쓰면 'am' 문자열이 들어가지만 extend를 쓰면 'a','m' 문자 하나씩 들어감
        while stack:
            print(stack.pop(), end='')
        print(end=' ')
    print('')


# 방법 2 - 스택 & append
for _ in range(T):
    words = input().strip()
    words += ' '
    for i in words:
        if i != ' ':
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end='')
            print(end=' ')
    print('')

# 방법 3 - 파이썬 문법 인덱스 슬라이스 reverse 사용
for _ in range(T):
    words = input().split()
    for i in words:
        print(i[::-1], end=' ')
    print('')
