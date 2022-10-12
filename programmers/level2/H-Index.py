# [Prog] 정렬 - lv2: H-Index

# 내림차순 정렬해서 찾는 법 ('6 5 4 1 0' => 인용 횟수 값이 논문 개수 보다 언제 작아지는지)
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if (i + 1) <= citations[i]:
            answer = i + 1
        if (i + 1) > citations[i]:
            break
    return answer

# 오름차순 정렬해서 찾는 법 ('0 1 4 5 6' => 인용 횟수 값이 남아있는 논문의 개수 보다 크거나 같은가?)
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0