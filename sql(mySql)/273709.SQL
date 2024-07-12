-- 코드를 작성해주세요
SELECT SUM(i.price) as 'TOTAL_PRICE'
FROM item_info i
WHERE i.rarity = 'LEGEND'