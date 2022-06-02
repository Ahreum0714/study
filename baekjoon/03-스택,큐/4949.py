import sys
sys.stdin = open("input.txt", "r")

while True:
    s = input()
    if s == '.':
        break
    else:
        str = s.split('.')
        ans = ''
        stack = []
        for i in str[0]:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) == 0 or stack[-1] == '[':
                    ans += 'no'
                    break
                elif stack[-1] == '(':
                    stack.pop()
            elif i == ']':
                if len(stack) == 0 or stack[-1] == '(':
                    ans += 'no'
                    break
                elif stack[-1] == '[':
                    stack.pop()
        
        if ans == '' and len(stack) == 0:
            ans += 'yes'
        elif ans == '' and len(stack) > 0:
            ans += 'no'
        
        print(ans)