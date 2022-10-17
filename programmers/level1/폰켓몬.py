def solution(nums):
    N = len(nums)
    typeArr = set(nums)
    if len(typeArr) < N/2:
        return len(typeArr)
    else:
        return N/2
    
# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))