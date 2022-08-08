import time
import sys
start = time.time()
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
people = [p for p in range(1,N+1)]
target = 0  # 제거할 인덱스
answer = []

while people:
    target += K - 1
    if target >= len(people):  # 제거할 인덱스의 크기가 남은 큐의 길이보다 클 경우
        target = target % len(people) # 한바퀴 돌았기 때문에 모듈러 연산으로 target을 재정의한다
    answer.append(str(people.pop(target)))

print(f'<{", ".join(answer)}>')

end = time.time()
print(f'{end-start:.6f} sec') # 백준 채점 결과 72ms 소요