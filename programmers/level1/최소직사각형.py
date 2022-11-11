# [Prog] 완전탐색 - lv1: 최소 직사각형

def solution(sizes):
    w_li = []
    h_li = []
    for w, h in sizes:
        if w > h:
            w_li.append(w)
            h_li.append(h)
        else:
            w_li.append(h)
            h_li.append(w)
            
    return max(w_li) * max(h_li)
