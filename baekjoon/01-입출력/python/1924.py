x, y = map(int, input().split())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
weekday = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
total_days = 0

for i in range(0, x-1):
    total_days += days[i]

total_days += y

k = total_days % 7
print(weekday[k])

