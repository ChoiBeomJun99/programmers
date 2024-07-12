-- 코드를 작성해주세요
SELECT year AS 'YEAR', max_size - size_of_colony AS 'YEAR_DEV', id
# - e.size_of_colony as "YEAR_DEV", e.id
FROM ecoli_data e1 JOIN (SELECT YEAR(differentiation_date) AS "year", MAX(size_of_colony) AS 'max_size'
                        FROM ecoli_data 
                        GROUP BY YEAR(differentiation_date)) AS e2 ON YEAR(e1.differentiation_date) = e2.year
ORDER BY 1, 2;