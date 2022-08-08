from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
stack = deque()
for _ in range(N):
    c = input().split()
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        # `if stack:` 이렇게 쓰는 것보다 len() 쓰는게 실행시간 조금 더 단축 됨
        if len(stack) == 0: print(-1)
        else:   print(stack.popleft())
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0: print(1)
        else:   print(0)
    elif c[0] == 'front':
        if len(stack) == 0: print(-1)
        else:   print(stack[0])
    elif c[0] == 'back':
        if len(stack) == 0: print(-1)
        else:   print(stack[-1])