-- 코드를 작성해주세요
SELECT e.id, IF(e.per <= 0.25, 'CRITICAL', 
             IF(e.per <= 0.5, 'HIGH', 
             IF(e.per <= 0.75, 'MEDIUM', 'LOW'))) AS 'COLONY_NAME'
FROM ( 
    SELECT id, PERCENT_RANK() OVER (ORDER BY size_of_colony DESC) AS 'PER'
    FROM ecoli_data
) AS e
ORDER BY e.id;