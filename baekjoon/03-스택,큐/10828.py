from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    query = input().split()
    if query[0] == 'push':
        stack.append(query[1])
    if query[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if query[0] == 'size':
        print(len(stack))
    if query[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if query[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])