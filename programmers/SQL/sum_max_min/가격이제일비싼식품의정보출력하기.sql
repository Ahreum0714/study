-- [Prog] SQL - lv2: 가격이 제일 비싼 식품의 정보 출력하기

-- 1. subquery
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
WHERE PRICE=(
    SELECT MAX(PRICE)
    FROM FOOD_PRODUCT
    )
    
-- 2. limit
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC LIMIT 1