import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
seq = list(map(int, input().split()))
stack = []     # 수열의 원소 인덱스를 담기 위한 스택
ans = [-1] * N # 수열의 각 원소에 대한 오큰수를 담기 위한 리스트

stack.append(0) # 0: 수열의 첫 원소 인덱스로 스택 초기화

# 입력받은 수열을 순회하면서 각각의 원소에 대응되는 오큰수 찾기
for i in range(1, N):
    while stack and seq[stack[-1]] < seq[i]: # 스택에 담긴 인덱스(원소)의 오큰수를 찾았으므로 
        ans[stack.pop()] = seq[i]            # 인덱스를 pop 하고, 찾은 오큰수 기록
    
    stack.append(i) # 오큰수를 아직 찾지 못한 인덱스는 스택에 push

print(*ans)