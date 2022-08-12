# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1918
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def solution(s):
    st = []
    ans = ''
    for c in s:
        if c.isalpha():
            ans += c
        elif c == '(':
            st.append(c)
        elif c == '*' or c == '/':
            while st and (st[-1] == '*' or st[-1] == '/'):
                ans += st.pop()
            st.append(c)
        elif c == '+' or c == '-':
            while st and st[-1] != '(':
                ans += st.pop()
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()
    while st:
        ans += st.pop()
    print(ans)

for tc in range(4):
    s = list(input().strip())
    solution(s)