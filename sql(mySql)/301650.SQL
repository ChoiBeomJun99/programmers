-- 코드를 작성해주세요
# 3세대 
SELECT e3.id
FROM ecoli_data e3
WHERE e3.parent_id in (SELECT e2.id # 2세대
                       FROM ecoli_data e2
                       WHERE e2.parent_id in (SELECT e1.id # 1세대
                                              FROM ecoli_data e1
                                              WHERE e1.parent_id is NULL
                                             )
                      )
ORDER BY id;