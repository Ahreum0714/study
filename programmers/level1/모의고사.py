# [Prog] 완전탐색 - lv1: 모의고사

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            cnt[0] += 1
        if answers[i] == second[i % len(second)]:
            cnt[1] += 1
        if answers[i] == third[i % len(third)]:
            cnt[2] += 1
        
    mx = max(cnt)
    for idx in range(len(cnt)):
        if mx == cnt[idx]:
            answer.append(idx + 1)
            
    return answer

# ----------- 다른 사람 풀이 ----------- #
### enumerate() 함수 활용해서 인덱스와 원소를 동시 접근하면서 루프 돌리기 ###
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    return [idx + 1 for idx, s in enumerate(score) if s == max(score)]