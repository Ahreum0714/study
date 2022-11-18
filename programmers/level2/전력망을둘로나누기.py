# [Prog] 완전탐색 - lv2: 전력망을 둘로 나누기 https://school.programmers.co.kr/learn/courses/30/lessons/86971

## 나의 풀이: 완탐 + BFS
'''
1. 노드별 연결된 노드 정보 dict로 초기화
2. 모든 간선을 하나씩 끊어보며 두 트리의 노드 개수 차의 min 값을 구한다 (for문)
    2-1. 끊긴 후 나뉜 두 트리의 노드 개수를 각각 구한다 (BFS)
        - [v1, v2] 간선이 끊긴다면 두 트리의 시작점은 각각 v1과 v2이다
    2-2. 위에서 구한 개수의 차 abs를 구한다
    2-3. 모든 경우의 수 중 가장 작은 min 값이 답이 된다
'''
from collections import deque

def solution(n, wires):
    answer = int(1e9)
    dict = {i: [] for i in range(1, n+1)}
    for v1, v2 in wires:
        dict[v1].append(v2)
        dict[v2].append(v1)

    def bfs(st, cnt):
        q = deque([st])
        visited = [False for _ in range(n+1)]
        while q:
            next = q.popleft()
            visited[next] = True
            cnt += 1
            for i in dict[next]:
                if not visited[i]:
                    q.append(i)
        return cnt

    for v1, v2 in wires:
        dict[v1].pop(dict[v1].index(v2))
        dict[v2].pop(dict[v2].index(v1))

        diff = abs(bfs(v1, 0) - bfs(v2, 0))
        answer = min(answer, diff)

        dict[v1].append(v2)
        dict[v2].append(v1)

    return answer


## 다른 사람 풀이: union find 알고리즘 이용
'''
테스트케이스에서 실행속도는 내 코드가 더 빠르지만
union find 알고리즘을 통해 최소 차를 구할 수 있다는 새로운 접근법을 배움!
'''
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer