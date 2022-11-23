# https://www.acmicpc.net/problem/15657 N과 M(8) (84ms)
n,m = map(int, input().split())
li = sorted(list(map(int, input().split())))

s = []

def solution(depth):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if s and li[i] < s[-1]:
            continue
        s.append(li[i])
        solution(depth + 1)
        s.pop()
        
solution(0)