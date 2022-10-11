-- [Prog] SQL - lv2: 중복 제거하기
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- NULL도 하나의 DISTINCT 처리 된다
-- 하지만 COUNT 함수는 필드값이 들어있는 레코드를 세기 때문에, 필드값이 없는 즉, NULL 값인 레코드를 세지 않는다
-- 단, 유의할 점은 필드값을 넣지 않는 COUNT(*) 는 NULL이 있는 레코드도 숫자를 센다! => 여기선 where절 없어도 되지만 count(*)이라면 where절 필요!