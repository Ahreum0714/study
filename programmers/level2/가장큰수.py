# [Prog] 정렬 - lv2: 가장 큰 수
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

######## 참고 블로그: https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html #######
# 1. int형의 list를 map을 사용하여 string으로 치환한 뒤, list로 변환한다.
# 2. 변환된 num을 sort()를 사용하여 key 조건에 맞게 정렬한다.
#   2-1) lambda x : x * 3은 num 인자 각각의 문자열을 3번 반복한다는 뜻이다.
#   2-2) x * 3을 하는 이유?
#   2-3) num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
# 3. 문자열 비교는 ASCII 값으로 치환되어 정렬된다. 따라서 666, 101010, 222의 첫번째 인덱스 값으로 비교한다.
#   3-1) 6 = 86, 1 = 81, 2 = 82 이므로 6 > 2 > 1순으로 크다.
#   3-2) sort()의 기본 정렬 기준은 오름차순이다. 이를 reverse = True를 통해 내림차순 해준다
# 4. 이것을 ‘‘.join(num)을 통해 문자열을 합쳐주면 된다.
#   4-1) int로 변환한 뒤, 또 str로 변환해주는 이유?
#   4-2) 모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.