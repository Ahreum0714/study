import sys, time
start = time.time()
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def solution(S):
    print(S)
    stack = []
    ans = []
    flag = 1 # 0:태그 / 1:문자열

    for s in S:
        if s == '<': #태그의 시작
            while stack:
                ans.append(stack.pop())
            ans += s
            flag = 0
        elif s == '>': #태그의 마지막
            ans += s
            flag = 1
        elif s == ' ': #공백
            while stack:  #문자열 단어 구분의 공백이라면
                ans.append(stack.pop()) #스택 내의 문자열을 뒤집어준 뒤 공백을 concat해줘야 함
            ans += s  #태그 내의 공백이라면 그냥 공백만 concat
        elif flag == 0:  #태그 내용(알파벳/숫자)
            ans += s
        else:  #문자열 내용(알파벳/숫자)
            stack.append(s)

    #주어진 문자열 S에 대한 탐색이 끝났는데 스택에 내용이 남아있을 경우
    while stack:
        ans.append(stack.pop())

    print(''.join(ans))

# 입출력 테스트케이스 한번에 검사
for tc in range(7):
    S = input().strip()
    solution(S)

end = time.time()
print(f'{end-start:.6f} sec') # 백준 채점 결과 112ms 소요