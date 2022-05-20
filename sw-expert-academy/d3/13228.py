T=int(input())
for test_case in range(1, T+1):
  S=input()
  weekdays=["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
  idx = weekdays.index(S)
  left = 6 - idx
  if left == 0: print(f'#{test_case} 7')
  else: print(f'#{test_case} {left}'}
