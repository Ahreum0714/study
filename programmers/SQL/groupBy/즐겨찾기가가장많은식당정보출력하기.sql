-- [Prog] SQL - lv3: 즐겨찾기가 가장 많은 식당 정보 출력하기
SELECT A.FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO A
    INNER JOIN (
        SELECT FOOD_TYPE, MAX(FAVORITES) MF
        FROM REST_INFO
        GROUP BY FOOD_TYPE
    ) B ON A.FOOD_TYPE = B.FOOD_TYPE AND A.FAVORITES = B.MF
ORDER BY A.FOOD_TYPE DESC

-- 1. 음식종류별로 즐겨찾기수가 가장 많은 식당을 구한다 (종류별=그룹화)
-- 2. 1에서 구한 음식종류와 즐겨찾기수를 기준으로 조인해준다