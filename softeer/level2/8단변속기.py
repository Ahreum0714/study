# [Softeer] lv2: 8단 변속기
# https://softeer.ai/practice/info.do?idx=1&eid=408&sw_prbl_sbms_sn=100184
import sys
tc = list(map(int, input().split()))

asc = [0 for _ in range(len(tc) - 1)]
des = [0 for _ in range(len(tc) - 1)]
for i in range(len(tc) - 1):
    if tc[i] < tc[i+1]:
        asc[i] = 1
    else:
        des[i] = 1

if len(set(asc)) == 1 or len(set(des)) == 1:
    if asc[0]:  print('ascending')
    else:   print('descending')
else:
    print('mixed')