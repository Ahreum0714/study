-- [Prog] SQL - lv4: 서울에 위치한 식당 목록 출력하기
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO AS I
    INNER JOIN REST_REVIEW AS R
    ON R.REST_ID = I.REST_ID
WHERE I.ADDRESS LIKE '서울%'
GROUP BY R.REST_ID
ORDER BY SCORE DESC, I.FAVORITES DESC
-- 유형별로 sum/avg/count/min/max => GROUP BY로 컬럼 데이터 그룹화!!
-- 식당별 리뷰 평균 => 식당&리뷰 테이블 join -> 식당으로 그룹화 -> 리뷰 평균 계산