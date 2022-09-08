# https://www.acmicpc.net/problem/1463 일곱 난쟁이 (68ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
sum(아홉 난쟁이) - (가짜 난쟁이1 + 가짜 난쟁이2) = 100
'''
people = [int(input().rstrip()) for _ in range(9)]
total = sum(people)

for i in range(len(people)):
    for j in range(i+1, len(people)):
        expt1, expt2 = people[i], people[j]
        if total - (expt1 + expt2) == 100:
            ans = [people[k] for k in range(9) if people[k] != expt1 and people[k] != expt2]
            ans.sort()
            print(*ans, sep='\n')
            exit()