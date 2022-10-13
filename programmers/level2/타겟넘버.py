# [Prog] DFS/BFS - lv2: 타겟 넘버

# BFS
def solution(numbers, target):
    leaves = [0]
    for n in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + n)
            tmp.append(parent - n)
        leaves = tmp
    return leaves.count(target)

# DFS
def solution(numbers, target):
    answer = 0
    end = len(numbers)
    def dfs(idx, result):
        if idx == end:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    dfs(0, 0)
    return answer 

# 다른 사람 풀이 1
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
# 다른 사람 풀이 2
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)