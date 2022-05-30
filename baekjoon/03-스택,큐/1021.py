from collections import deque
import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
li = map(int, input().split())  # 추출해야하는 인덱스 타겟 리스트 입력받기

deq = deque(range(1, n+1))  # 입력받은 수열 양방향 큐 (큐의 값 = 가장 처음 큐에서의 위치)
cnt = 0

for target in li:
    # 최소 연산을 구하기 위한 중간 인덱스 mid
    mid = len(deq) // 2 
    if deq.index(target) <= mid:  # 인덱스 타겟 값의 현재 위치가 중간 인덱스보다 작거나 같다면
        while deq[0] != target:   # 2번 연산 수행 (왼쪽 이동)
            deq.append(deq.popleft())
            cnt += 1
        deq.popleft()
    else:                        # 인덱스 타겟 값의 현재 위치가 중간 인덱스보다 크다면
        while deq[0] != target: # 3번 연산 수행 (오른쪽 이동)
            deq.appendleft(deq.pop())
            cnt += 1
        deq.popleft()

print(cnt)