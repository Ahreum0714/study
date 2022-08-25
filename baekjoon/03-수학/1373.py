# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/1373 2진수8진수 (80ms)
import sys
sys.stdin = open('input.txt', 'r')

n = sys.stdin.readline()
print(oct(int(n, 2))[2:])  # 파이썬 내장함수로 2진법, 8진법 구할 수 있음! (2->8 직접하려면 세자리수씩 끊어서 구하면 될 것)