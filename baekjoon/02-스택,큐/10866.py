from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    query = input().split()
    if query[0] == 'push_front':
        deq.appendleft(query[1])
    if query[0] == 'push_back':
        deq.append(query[1])
    if query[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    if query[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    if query[0] == 'size':
        print(len(deq))
    if query[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if query[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if query[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])