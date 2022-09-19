# https://www.acmicpc.net/problem/6064 카잉달력 
import sys
sys.stdin = open('input.txt', 'r')
input = lambda: sys.stdin.readline()

########## 방법 1. (2548ms) ##########
'''
k = M*p + x = N*q + y
즉, (k-x)%m = 0 이면서 (k-y)%n =0 이다. 

단, k값을  0부터 x*y 까지 +1씩 증가시키며 돌면 시간초과가 발생한다. 
k는 M*p + x 또는 N*q + y 이므로,
(k-x)는 m의 배수 이고 (k-y)은 n의 배수이다.
즉, x, y 둘중 하나의 값만 이용해서 문제를 풀 수 있다.

(k-x)%m = 0 을 이용한다면,
k = x 이거나 k는 x+m 혹은 k는 x+2m..... 
즉, k를 x로 초기화 한 후 추가적으로 m만 더해주면 된다. 
'''
def cain(M, N, x, y):
    k = x
    # k의 범위는 M*N을 넘을 수 없음
    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            return k
        # (k-x)가 M의 배수이고, k는 x로 초기화해주었기 때문에 m만 더해준다
        k += M
    return -1

########## 방법 2. (1868ms) ##########
'''
(k-x)%m = 0
(k-y)%n = 0
k는 x에 m을 계속 더한 값이거나 y에 n을 계속 더한 값 중 하나이다.
    k = x + m*p = y + n*q
x를 고정시켜서 k값을 확인하자면,
    x + m*p - y = n*q
'''
def cain2(M, N, x, y):
    # k의 범위는 M*N을 넘을 수 없음
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(cain(M, N, x, y))


