# https://www.acmicpc.net/problem/15656 N과 M(7) (1712ms)
n,m = map(int, input().split())
li = sorted(list(map(int, input().split())))

s = []

def solution(depth):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        s.append(li[i])
        solution(depth + 1)
        s.pop()
        
solution(0)