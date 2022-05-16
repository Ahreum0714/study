import sys
sys.stdin = open("input.txt", "r")

def solve(N, k, total):
    # k: 1 <= k <= N
    # k_rank: k번째 학생의 총점 순위 (순위:0~N-1)
    desc_total = sorted(total, reverse=True)
    # k는 1부터 시작하지만, 리스트 인덱스는 0부터 시작하므로 k-1 (예: k=2라면 2번째 입력받은 학생 -> total[1]가 2번째 학생의 총점)
    k_score = total[k-1]
    k_rank = desc_total.index(k_score) 
    # 각 평점당 학생 수 ("//": 몫 연산자)
    n = N // 10
    # k번째 학생의 평점: "(순위) / (평점당 명수)" 의 몫 = 평점의 인덱스
    idx = k_rank // n
    return grade[idx]

T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] # 평점 순서 주의!...
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    total = [0] * N # total: 0번째부터 N-1번째 학생의 총점을 담고 있는 리스트
    for i in range(N):
        mid, fin, ass = map(int, input().split())
        total[i] += (mid * 0.35) + (fin * 0.45) + (ass * 0.2)
    result = solve(N, k, total)
    print(f'#{test_case} {result}')