def solution(n, k):
    result = ''
    answer = 0
    
    # 10진수에서 k진법으로 변환
    while n > 0:
        result = str(n%k) + result
        n = n // k
    
   # 조건에 맞는 소수 찾기
    numbers = result.split('0')
    for num in numbers:
        if not num:
            continue
        if int(num) <= 1:
            continue
            
        flag = True
        for i in range(2, int(int(num) ** 0.5) + 1): # 이 문제는 에라토스테네스의 체 사용 안해도 충분함
            if int(num) % i == 0:
                flag = False
                break
        if flag:
            answer += 1
            
    return answer