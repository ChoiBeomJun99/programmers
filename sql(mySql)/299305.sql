-- 코드를 작성해주세요
SELECT e.id, IFNULL(
                (SELECT count(*)
                 FROM ecoli_data e2
                 GROUP BY e2.parent_id
                 HAVING e2.parent_id = e.id
                 ), 0) AS 'CHILD_COUNT'
FROM ecoli_data e
ORDER BY e.id;