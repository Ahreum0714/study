import sys
sys.stdin = open("input.txt", "r")

N = int(input())
stack = []
ans = []
n = 1
flag = 0
for i in range(N):
    k = int(input())
    # 입력한 수 k 를 만날 때 까지 오름차순으로 스택에 값을 push
    while k >= n:
        stack.append(n)
        ans.append('+')
        n += 1
    
    # 스택의 top이 k 라면, pop 해서 수열 만들기
    if stack[-1] == k:
        stack.pop()
        ans.append('-')
    else:
        # 스택의 top이 k가 아니라면, 스택으로 수열을 만들 수 없음
        print('NO') # 스택은 top의 값만 빼낼 수 있기 때문.
        flag = 1 # 스택의 top이 k보다 클 경우, 스택 속 k는 top 아래에 있음
        break  # top을 빼기 전까지는 top 아래에 있는 k 값을 빼낼 수 없으므로, 수열을 완성할 수 없음
    
if flag == 0:
    for a in ans:
        print(a)

    
    