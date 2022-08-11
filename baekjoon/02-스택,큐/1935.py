# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1935
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
expression = list(input().strip())
operand = [chr(ord('A')+i) for i in range(N)]
num = [0] * N
st = []
for _ in range(N):
    num[_] = int(input())

for c in expression:
    if c in operand:
        st.append(num[operand.index(c)])
    else:
        r = st.pop()
        l = st.pop()
        if c == '+':
            st.append(l + r)
        if c == '-':
            st.append(l - r)
        if c == '*':
            st.append(l * r)
        if c == '/':
            st.append(l / r)

print(f'{st.pop():.2f}')