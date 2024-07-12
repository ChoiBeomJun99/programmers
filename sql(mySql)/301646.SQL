-- 코드를 작성해주세요
SELECT COUNT(*) AS 'COUNT'
FROM ecoli_data e
WHERE 1=1
AND e.genotype & 2 != 2
AND ((e.genotype & 1 = 1) OR (e.genotype & 4 = 4))