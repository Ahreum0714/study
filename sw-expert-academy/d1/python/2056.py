import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    m = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    d = ["31","28","31","30","31","30","31","31","30","31","30","31"]
    date = input()
    year = date[0:4]
    month = date[4:6]
    day =date[6:]

    result = ""
    if int(year) > 0 and month in m:
        m_idx = m.index(month)
        if day <= d[m_idx]:
            result += year + '/' + month + '/' + day
        else: result += str(-1)
    else: result += str(-1)

    print(f'#{test_case} {result}')