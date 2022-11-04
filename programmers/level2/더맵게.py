# [Prog] 힙 - lv2: 더맵게 https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
        
    return answer if scoville[0] >= K else -1


# 다른 사람 풀이) while True + if문
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
        
    return answer

# 다른 사람 풀이) 조건문 대신 try-except
from heapq import heapify, heappush, heappop
def solution(scoville, K):
    heapify(scoville)
    for i in range(1000000):
        try:
            heappush(scoville, heappop(scoville)+(heappop(scoville)*2))
            if scoville[0] >= K: return i+1
        except:
            return -1