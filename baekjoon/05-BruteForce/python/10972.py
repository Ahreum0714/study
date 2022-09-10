# https://www.acmicpc.net/problem/10972 다음 순열 (72ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
 <<itertools의 permutations로 구하면 메모리초과가 발생된다. 따라서 next_permutation 알고리즘을 직접 구현해야한다.>>
  참고: https://ji-gwang.tistory.com/262
1 4 3 2를 예시로 알고리즘을 알아본다.
    1. 뒤에서부터 순열을 비교하며, 뒷 값이 앞 값보다 큰 경우까지 반복한다. (3,2), (4,3)은 해당하지 않고, (1,4)가 해당된다. 
        a .이 때, 1의 인덱스를 x라고 칭한다.
        b. 4의 인덱스는 y라고 한다.
    2. 다시 뒤에서부터 값을 비교하며 인덱스 x보다 큰 값이 있으면 그 값과 swap한다.
        a.1과 2를 비교했고, 2가 크기 때문에 이 둘을 swap한다.
    3. y에 해당하는 인덱스부터 sort(오름차순정렬)를 한 뒤에 이어 붙인다.
        a. 4 3 1을 sort해서 1 3 4가 된다.
        b. 이어 붙이기 때문에 2 1 3 4가 된다.
'''
n = int(input())
seq = list(map(int, input().split()))
# 뒤에서부터 둘씩 비교해가며, 뒷 값이 앞 값보다 큰 경우까지 반복
for i in range(n-1, 0, -1):
    if seq[i-1] < seq[i]:   # 앞 값(x)이 뒷 값(y)보다 작을 때
        for j in range(n-1, 0, -1): # 뒤에서부터 순회를 다시 시작하여
            if seq[i-1] < seq[j]:   # 그 앞 값(x)보다 큰 값이 뒤에 있다면 swap 해주고
                seq[i-1], seq[j] = seq[j], seq[i-1]
                seq = seq[:i] + sorted(seq[i:]) # (y)부터 끝까지의 부분순열을 오름차순 정렬하고 이어 붙이기
                print(*seq)
                exit()
print(-1)
