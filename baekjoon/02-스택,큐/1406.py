import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []
M = int(input())

for _ in range(M):
    command = list(input().split())
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])

stack1.extend(reversed(stack2))
print(''.join(stack1))
