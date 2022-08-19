# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1929
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 아리스토테네스의 체 (소수 구하기)
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

m, n = map(int, input().split())
ans = []
for i in range(m, n+1):
    if isPrime(i):
        print(i)
# (3752ms)


## 다른 사람 풀이 (320ms)
def solve():
  M, N = map(int, sys.stdin.readline().rstrip().split())
  primes = [True] * (N+1)
  primes[1] = False
  for i in range(2, N+1):
    if primes[i]:
      for j in range(i*2, N+1, i):
        primes[j] = False
  for i in range(M, N+1):
    if primes[i]:
      print(i)
 
solve()