-- 코드를 입력하세요
SELECT book_id, to_char(published_date, 'YYYY-MM-DD') as published_date
FROM BOOK
WHERE 1=1
and to_char(published_date, 'YYYY') = '2021'
and category = '인문'
order by published_date;