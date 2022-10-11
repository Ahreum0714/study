def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    return answer

# 다른 사람 풀이 1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 다른 사람 풀이 2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer