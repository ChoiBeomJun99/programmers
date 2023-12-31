-- 코드를 입력하세요
SELECT YEAR(O.SALES_DATE) AS YEAR, MONTH(O.SALES_DATE) AS MONTH, COUNT(DISTINCT O.USER_ID) AS 'PUCHASED_USERS',
ROUND(COUNT(DISTINCT O.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE YEAR(JOINED) = 2021), 1) AS 'PUCHASED_RATIO'
FROM USER_INFO U JOIN ONLINE_SALE O ON U.USER_ID = O.USER_ID
# 2021년에 가입하고 상품을 매한 회원 수
WHERE YEAR(U.JOINED) = 2021 AND U.USER_ID IN (SELECT USER_ID FROM ONLINE_SALE)
GROUP BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE)
ORDER BY 1, 2;