# https://www.acmicpc.net/problem/14888 연산자 끼워넣기 (60ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
operator = list(map(int, input().split())) # 연산자: +, -, *, //

maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, division):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    
    if plus:
        dfs(depth+1, total+seq[depth], plus-1, minus, multiply, division)
    if minus:
        dfs(depth+1, total-seq[depth], plus, minus-1, multiply, division)
    if multiply:
        dfs(depth+1, total*seq[depth], plus, minus, multiply-1, division)
    if division:
        dfs(depth+1, int(total/seq[depth]), plus, minus, multiply, division-1)
        ### 양수 나눗셈은 "//"와 "int()" 연산자의 결과가 같지만, 음수의 경우는 다름!!!!
        ### "//" 연산자는 나누기 결과보다 작은 정수 중 가장 큰 정수가 결과값 (eg. -10//3 = -4)
        ### "int()" 연산자는 소수 부분을 버린다. (eg. int(-10/3) = -3)

dfs(1, seq[0], operator[0], operator[1], operator[2], operator[3])

print(maximum, minimum, sep='\n')