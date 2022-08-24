# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/2004 조합 0의 개수
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def countNum(N, num):
    count = 0
    divNum = num
    while( N >= divNum):
        count = count + (N // divNum)
        divNum = divNum * num
    return count

M, N = map(int, input().split())

print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))

# 참고: https://somjang.tistory.com/entry/BaeKJoon-2004%EB%B2%88-%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-Python