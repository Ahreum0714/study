# [Prog] DFS/BFS - lv3: 여행경로 https://school.programmers.co.kr/learn/courses/30/lessons/43164
def solution(tickets):
    answer = []

    # 1. 그래프 생성
    routes = {}
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]
    # 2. 시작점 - [도착점] 역순 정렬
    for k in routes.keys():
        routes[k].sort(reverse=True)
    
    # 3. DFS 알고리즘 & stack 으로 path 생성
    st = ['ICN']
    while st:
        top = st[-1]    
        if top not in routes or len(routes[top]) == 0:
            answer.append(st.pop())
        else:
            st.append(routes[top].pop())
    
    # 4. stack 뒤에서 부터 pop해서 answer를 붙였으므로 다시 거꾸로 뒤집어서 순서 맞추기
    return answer[::-1]