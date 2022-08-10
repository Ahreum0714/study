import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
ans = [-1] * N

for i in range(N-1):
    stack.append(i)
    while stack and A[stack[-1]] < A[i+1]:
        ans[stack.pop()] = A[i+1]
    
print(*ans)

## 예전 코드(17298.py)가 조금 더 나은 듯? 인덱스[i+1]하지 않아도 되니까