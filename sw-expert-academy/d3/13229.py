import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
  S = input()
  weekdays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
  idx = weekdays.index(S)
  left = 7 - idx
  print(f'#{test_case} {left}')
