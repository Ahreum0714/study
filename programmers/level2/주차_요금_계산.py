############ 다른 사람 풀이 - 제일 깔끔하고 가독성 좋은 듯 ############
# class, defaultdict, flag 등을 활용해서 객체지향적으로, 로직을 바로 알 수 있게 작성한게 인상적이다
from collections import defaultdict
from math import ceil

class Parking:
    def __init__(self, fees):
        self.fees = fees
        self.in_flag = False
        self.in_time = 0
        self.total = 0

    def update(self, t, inout):
        self.in_flag = True if inout=='IN' else False
        if self.in_flag:  self.in_time = str2int(t)
        else:             self.total  += (str2int(t)-self.in_time)

    def calc_fee(self):
        if self.in_flag: self.update('23:59', 'out')
        add_t = self.total - self.fees[0]
        return self.fees[1] + ceil(add_t/self.fees[2]) * self.fees[3] if add_t >= 0 else self.fees[1]

def str2int(string):
    return int(string[:2])*60 + int(string[3:])

def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for rcd in records:
        t, car, inout = rcd.split()
        recordsDict[car].update(t, inout)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]


############ 나의 풀이 ############
# 위의 풀이와 비교해보면 다소 직관적이지 못한 로직으로 아쉬운 점이 보이는 듯
# 주석이 없다면 코드만으로는 이해하는데 시간이 걸릴 수 있을 것 같다는 점?
import math

def hours_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def calculate(times, fees):
    base_time, base_fee, unit_time, unit_fee = fees
    total_time, in_time, out_time = 0, 0, 0
    # 누적 주차 시간 계산
    for t in range(len(times)):
        if t % 2:
            out_time = times[t]
            total_time += out_time - in_time
        else:
            in_time = times[t]
    # 요금 계산
    if total_time <= base_time:
        return base_fee
    else:
        return base_fee + math.ceil((total_time - base_time)/unit_time) * unit_fee

def solution(fees, records):
    cars = set([r.split()[1] for r in records])
    info = {car: [] for car in cars}
    answer = []

    # 차량별 입출차 기록 저장
    for r in records:
        info[r.split()[1]].append(hours_to_minutes(r.split()[0]))

    # OUT이 없는 차량은 23:59 OUT 으로 계산 (OUT이 없는 경우는 무조건 홀수라는 점에 착안)
    for car in cars:
        if len(info[car]) % 2:
            info[car].append(23*60 + 59)

    # 주차요금 계산
    for car in cars:
        info[car] = calculate(info[car], fees)

    # 차량 번호가 작은 자동차 순으로 주차요금 정렬
    for i in sorted(info.items()):
        answer.append(i[1])

    return answer