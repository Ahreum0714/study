# https://www.acmicpc.net/problem/2501 약수 구하기 (44ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
divisor = []

for i in range(1, n+1):
    if n % i == 0:  divisor.append(i)

if len(divisor) >= k:
    print(divisor[k-1])
else:
    print(0)
    
''' 다른 사람 풀이 '''
# n,k=map(int,input().split())
# a=0
# for i in range(1,n+1):
#     if n%i==0:
#         a+=1
#         if a==k:
#             print(i)
#             break
# if a<k:
#     print(0)
''' 굳이 list 로 공간 잡을 필요 없이 바로 출력도 가능! '''