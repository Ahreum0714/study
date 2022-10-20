def solution(clothes):
    answer = 1
    closet = {}
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])
        else:
            closet[cloth[1]] = [cloth[0]]
    
    for value in closet.values():
        answer *= len(value) + 1  #의상 종류별로 안 입는 경우의 수(1)를 추가해 모든 경우의 수 구하기
    
    return answer - 1  #아무것도 입지 않는 경우 제외