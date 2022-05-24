from itertools import combinations, permutations
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = list(x for x in input())        # 입력받은 문자열을 문자리스트로 변환
    target = [i for i in range(len(N))] # 바꿀 문자의 인덱스를 추출하기 위한 리스트
    
    min_num, max_num = int(''.join(N)), int(''.join(N))

    for value in combinations(target, 2):  # 순서는 중요하지 않으므로 permutations(순열) 대신 combinations(조합)
        i, j = value
        N[i], N[j] = N[j], N[i]
        if N[0] == '0':
            N[i], N[j] = N[j], N[i]
            continue
        if int(''.join(N)) < min_num:
            min_num = int(''.join(N))        
        if int(''.join(N)) > max_num:
            max_num = int(''.join(N))        
        N[i], N[j] = N[j], N[i]
        
    print(f'#{test_case} {min_num} {max_num}')