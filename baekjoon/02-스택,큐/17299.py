# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/17299
import sys, copy
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
F = [0] * 1000001
st = copy.deepcopy(A)
ans = [-1] * N

while st:
    F[st.pop()] += 1

st.append(0)
for i in range(1, N):
    while st and F[A[st[-1]]] < F[A[i]]:
        ans[st.pop()] = A[i]
    st.append(i)

print(*ans) # python3: 2088ms / pypy3: 740ms