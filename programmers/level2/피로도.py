from itertools import permutations

def solution(k, dungeons):
    answer = -1
    order = list(permutations(dungeons, len(dungeons)))
    for o in order:
        tmp = k
        cnt = 0
        for min, quantity in o:
            if tmp >= min:
                tmp -= quantity
                cnt += 1
                answer = max(answer, cnt)
    return answer
