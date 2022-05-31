import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

K = int(input())

stack = []
for _ in range(K):
    x = int(input())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))