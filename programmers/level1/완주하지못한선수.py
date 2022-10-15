# hash 이용
def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for p in participant:
        hashDict[hash(p)] = p
        sumHash += hash(p)
    for c in completion:
        sumHash -= hash(c)
    
    return hashDict[sumHash]

# Counter 이용
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]