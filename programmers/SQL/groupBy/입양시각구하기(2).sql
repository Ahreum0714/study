-- [Prog] SQL - lv4: 입양 시각 구하기(2)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59413

-- 1. SET 구문을 이용한 변수 선언으로 ANIMAL_OUTS 테이블에 포함되지 않은 시간 데이터도 조회
SET @Hour = -1; -- 변수 선언

SELECT (@Hour := @Hour + 1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME))
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @Hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @Hour < 23

-- 2. WITH RECURSIVE & UNION 함수 사용으로 ANIMAL_OUTS 테이블에 포함되지 않은 시간 데이터도 조회
-- UNION : 결합시 중복 제거
-- UNION ALL : 결합시 중복 제거 X
-- 0~23 row 테이블 만들고 left join
WITH RECURSIVE TIME AS (
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR + 1 FROM TIME WHERE HOUR < 23)

SELECT TIME.HOUR, COUNT(ANIMAL_OUTS.DATETIME) AS COUNT
FROM TIME LEFT JOIN ANIMAL_OUTS
ON TIME.HOUR = HOUR(ANIMAL_OUTS.DATETIME)
GROUP BY HOUR;