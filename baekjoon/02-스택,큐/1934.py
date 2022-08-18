# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1934
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def gcd(a,b): # 유클리드 호제법 (a와 b (a > b)가 있다고 할 때, a와 b의 최대공약수 G는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 G'과 서로 같다)
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a,b): # (최소공배수 x 최대 공약수) = gcd^2 * a * b [a, b은 서로수] => a * b 이용
    return a * b // gcd(a,b)

T = int(input())
for _ in range(T):
    a, b = map(int, input().strip().split())
    print(lcm(a,b))