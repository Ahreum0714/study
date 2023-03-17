# https://www.acmicpc.net/problem/2581 소수 (44ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

SIZE = 10000
m = int(input())
n = int(input())
prime_num = [False] + [True for _ in range(SIZE)]
prime_num[1] = False

def find_prime(max_num):
    for i in range(2, max_num+1):
        if prime_num[i]:
            for j in range(2, max_num//i+1):
                prime_num[i*j] = False

def print_ans():
    sum, min = 0, 0
    for candidate in range(m, n+1):
        if prime_num[candidate]:
            sum += candidate
            if min == 0:
                min = candidate

    if sum == 0 and min == 0:
        print(-1)
    else:
        print(sum, min, sep='\n')

find_prime(SIZE)
print_ans()