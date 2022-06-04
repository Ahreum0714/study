import sys
sys.stdin = open("input.txt", "r")

N = int(input())
stack = []
ans = []
n = 1
flag = 0
for i in range(N):
    k = int(input())
    while k >= n:
        stack.append(n)
        ans.append('+')
        n += 1
    
    if stack[-1] == k:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        flag = 1
        break
    
if flag == 0:
    for a in ans:
        print(a)

    
    