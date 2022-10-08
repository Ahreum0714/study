-- [Prog] SQL - lv1: 여러 기준으로 정렬하기
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME ASC, DATETIME DESC
-- 이름으로 오름차순하고, 같은 이름이 있을 경우 보호시작일을 기준으로 내림차순해서 보여준다