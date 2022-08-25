# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/17087 숨바꼭질6 (124ms)
from math import gcd
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 1. a 원소 각각마다 (s - a 원소)의 차를 모두 구한다
# 2. 차들의 최대 공약수를 구한다
n, s = map(int, input().split())
a = list(map(int, input().split()))

difference = [abs(s-i) for i in a]
ans = difference[0]
for i in range(1, len(difference)):
    ans = gcd(ans, difference[i])

print(ans)

'''
----람다식을 활용한 다른 사람 풀이----
from math import gcd
N, S = map(int, input().split(" "))
pos = list(map(lambda x: abs(int(x)-S), input().split()))
print(gcd(*pos))
----------------------------------
    #python3.9부터 math.gcd()의 argument 개수가 2개 이상도 가능해짐! 
    # 내 로컬 버전은 3.8.10이라 안됨..
    # 참고: 백준 컴파일 버전은 3.10.4
'''