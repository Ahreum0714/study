-- [Prog] SQL - lv2: 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- COUNT(*)    // 이렇게도 가능
-- ORDER BY 1  // 여기선 이렇게 해도 됨. 첫 번째 열을 기준으로 정렬하란 뜻이기 때문