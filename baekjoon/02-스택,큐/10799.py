import sys, time
start = time.time()
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 알고리즘 문제 풀이 https://www.acmicpc.net/problem/10799
def solution(s):
    stack = []
    result = 0

    for i in range(len(s)):
        # 막대 시작
        if s[i] == '(':    
            stack.append(i)
        else:
            # 레이저
            if s[i-1] ==  '(':
                stack.pop()
                result += len(stack)
            # 막대 끝
            else: 
                result += 1
                stack.pop()
    return result

# 입출력 테스트케이스 일치 검사
for tc in range(2):
    s = list(input().split())
    ans = solution(s[0])
    print(f'#{tc+1}: {ans == int(s[1])}')

end = time.time()
print(f'{end-start:.6f} sec') # 백준 채점 결과 96ms 소요


# # 백준 제출 코드: 96ms
# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

# s = list(input().strip())
# stack = []
# result = 0

# for i in range(len(s)):
#     # 막대 시작
#     if s[i] == '(':    
#         stack.append(i)
#     else:
#         # 레이저
#         if s[i-1] ==  '(':
#             stack.pop()
#             result += len(stack)
#         # 막대 끝
#         else: 
#             result += 1
#             stack.pop()
# print(result)