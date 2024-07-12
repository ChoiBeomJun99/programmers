-- 코드를 작성해주세요
SELECT e.id, IF(e.size_of_colony <= 100, 'LOW', IF(e.size_of_colony > 100 AND e.size_of_colony <= 1000, 'MEDIUM', 'HIGH')) AS 'SIZE'
FROM ecoli_data e
ORDER BY id;