from collections import deque

N, K = map(int,input().split())
q = deque([_ for _ in range(1, N+1)])
ans = []
while q:
    q.rotate(-K)
    target = q.pop()
    ans.append(target)

print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print(f'{ans[-1]}>')