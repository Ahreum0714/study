# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/6588 골드바흐의 추측
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 골드바흐의 추측 검증
def goldbach(prime, num):
    for i in range(3, len(prime)):
        if prime[i] and prime[num-i]:
            return f'{num} = {i} + {num-i}'
    return "Goldbach's conjecture is wrong."

# 소수 리스트 구하기 (sqrt로 구하니까 시간 초과 오류남)
prime_li = [True for _ in range(1000001)]
for i in range(2, 1001):
    if prime_li[i]:
        for j in range(i+i, 1000001, i):
            prime_li[j] = False

while True:
    n = int(input())

    if n == 0:  exit()

    ans = goldbach(prime_li, n)
    print(ans)