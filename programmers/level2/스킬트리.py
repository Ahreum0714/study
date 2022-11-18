# [Prog] 구현 - lv2: 스킬트리 https://school.programmers.co.kr/learn/courses/30/lessons/49993

# 내가 짠 코드
def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:        
        sk = ''.join([c for c in skill_tree if c in skill ])        
        flag = True
        for i, val in enumerate(sk):
            if val != skill[i]:
                flag = False
                break
        if flag:
            answer += 1
            
    return answer
'''
=> 다른 사람이 작성한 코드의 아이디어 접근 법이나 로직은 동일/유사한 것으로 보임!
다만 내가 작성한 코드는 가독성면에서 더 다듬을 필요가 있는 코드 같음

=> [배운점]
파이썬에는 if-else 뿐만 아니라 for-else 구문이 있다!!!
번거롭게 flag를 사용하지 않아도 된다!!
else문에 break없이 빠져나온 경우를 작성하면 끝!
'''

# 다른 사람 코드 1
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
'''
skill에 속하는 문자열을 뽑아내 따로 저장하고 skill과 비교하는 방식이 아니라,
스킬트리에서 바로 검사하기 위해 skill과 같은 리스트를 하나 더 생성한 뒤 pop()을 이용한 듯!
'''

# 다른 사람 코드 2
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer
'''
=> 스킬트리에서 skill에 속한 스킬 문자를 따로 모아 저장한다는 점은 나랑 동일하고,
다른 점은 나는 '인덱스'를 통해 하나하나 비교대조했다면,
이 분은 '슬라이싱'을 통해 따로 모아 저장한 문자열의 길이만큼 skill과 한번에 비교했다는 점
'''