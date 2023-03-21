# https://www.acmicpc.net/problem/14888 괄호의 값 (44ms)
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
'''
(()[[]])
= 2*{()[[]]}
= 2*{2+[[]]}
= 2*{2+[3]}
= 2*{2+3*3}
= 2*2 + 2*3*3 (분배법칙)

즉, 괄호 쌍 성립 여부 판단을 위한 스택 st, 총합의 변수 ans, 그리고 별도의 괄호열 계산을 위한 변수 tmp가 필요함
1. ( : tmp에 2를 곱해주면서 스택에 괄호 push
2. [ : tmp에 3을 곱해주면서 스택에 괄호 push
3. ) : 
    3-1. 스택이 비어있다면 닫을 괄호가 없으므로 올바르지 못한 괄호열이다.
    3-2. 스택의 top이 '('가 아닌 다른 괄호열이라 닫을 수 없어도 올바르지 못한 괄호열이다.
    3-3. 스택의 top이 '('라면, '()'괄호 쌍을 만들 수 있다.
        => 바로 이전 괄호또한 '('라면, 하나의 괄호열 묶음을 다 구한 것이므로 누적계산된 tmp 값을 ans에 더해준다. 
        => 위에서 해당 괄호열 묶음의 계산을 이미 끝냈으므로 다음 괄호열 묶음 계산을 위해 tmp을 원위치 시켜줘야한다.
        => 해당 괄호열 묶음의 값만큼 나눠줘야하므로, 성립됐던 괄호 쌍의 개수만큼 tmp에  //2 해줘야 한다.
        => 즉, 이전 괄호가 '('이든 아니든 상관없이 현재 괄호가 ')'이고 스택의 top이 '('일 때마다 tmp에 //2 해주면 된다.
4. ] : 3번과 같되 '[]'괄호 쌍이 만들어지면 //3 해준다는 차이만 있다.
'''
bracket = input()
st = []
ans = 0
tmp = 1

for i in range(len(bracket)):
    if bracket[i] == '(':
        st.append(bracket[i])
        tmp *= 2
    elif bracket[i] == '[':
        st.append(bracket[i])
        tmp *= 3
    elif bracket[i] == ')':
        if not st or st[-1] == '[':
            print(0)
            exit()
        if bracket[i-1] == '(':
            ans += tmp
        st.pop()
        tmp //= 2
    elif bracket[i] == ']':
        if not st or st[-1] == '(':
            print(0)
            exit()
        if bracket[i-1] == '[':
            ans += tmp
        st.pop()
        tmp //= 3
    
if st:
    print(0)
else:
    print(ans)