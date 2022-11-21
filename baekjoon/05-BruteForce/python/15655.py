# https://www.acmicpc.net/problem/15655 N과 M(6) (68ms)
n,m = map(int, input().split())
li = sorted(list(map(int, input().split())))

s = []

def solution(depth):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if li[i] in s: # 중복 선택 방지
            continue
        if s and li[i] < s[-1]: # 비오름차순 조건 배제
            continue
        s.append(li[i])
        solution(depth + 1)
        s.pop()
        
solution(0)