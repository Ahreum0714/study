import sys
sys.stdin = open("input.txt", "r")

t = int(input())
for _ in range(t):
    stack = []
    vps = ''
    parenthesis = input()
    for p in parenthesis:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                vps += 'NO'
                break
    
    if vps == '' and len(stack) == 0:
        vps += 'YES'
    elif vps == '' and len(stack) > 0:
        vps += 'NO'
    
    print(vps)