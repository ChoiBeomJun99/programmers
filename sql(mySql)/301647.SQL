-- 코드를 작성해주세요
SELECT e1.id, e1.genotype, e2.genotype AS 'PARENT_GENOTYPE'
FROM ecoli_data e1 JOIN ecoli_data e2 ON e1.parent_id = e2.id
WHERE e1.genotype & e2.genoType >= e2.genoType
ORDER BY id;

# 부모 1011
# 자식 1111 o 

# 부모 1001
# 자식 1000 x