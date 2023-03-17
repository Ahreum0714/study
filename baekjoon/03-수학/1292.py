# https://www.acmicpc.net/problem/1292 쉽게 푸는 문제 (40ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

a, b = map(int, input().split())
sequence = [0]

for i in range(1, b+1):
    sequence += [i for _ in range(i)]
    if len(sequence) > 1000: break

print(sum(sequence[a:b+1]))

### 처음 풀이 (48ms) ###
# --> b가 1000일 경우 수열의 1000번째 자릿수만 알면 되는데 그 이상의 크기까지 수열을 만들 수 있어 비효율적이라 판단함
'''
a, b = map(int, input().split())
sequence = [0]

for i in range(1, b+1):
    sequence.extend([i]*i)

print(sum(sequence[a:b+1]))
'''