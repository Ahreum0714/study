# https://www.acmicpc.net/problem/15654 N과 M(5) (ms)

n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))

s = []

def solution(depth):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if li[i] in s: # 중복 선택 방지
            continue
        s.append(li[i])
        solution(depth + 1)
        s.pop()
        
solution(0)